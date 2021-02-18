package main

import (
	"context"
	"fmt"
	"github.com/gin-contrib/cors"
	"github.com/gin-contrib/sessions"
	"github.com/gin-contrib/sessions/redis"
	"github.com/gin-gonic/gin"
	_ "github.com/lib/pq"
	"go-message/config"
	"go-message/ent"
	"go-message/middlewares"
	"go-message/routes"
	"log"
	"time"
)

func getDbConfig() string {
	dbConfig := config.Config.Database
	return fmt.Sprintf("host=%s port=%s user=%s dbname=%s password=%s sslmode=disable\n",
		dbConfig.Host,
		dbConfig.Port,
		dbConfig.Username,
		dbConfig.Name,
		dbConfig.Password)
}

func getRedisConfig() (redis.Store, error) {
	redisConfig := config.Config.Redis
	address := fmt.Sprintf("%s:%s", redisConfig.Host, redisConfig.Port)
	return redis.NewStore(
		10,
		"tcp",
		address,
		redisConfig.Password,
		[]byte(redisConfig.Secret),
	)
}

func main() {
	time.Sleep(time.Second * 1)
	r := gin.Default()

	store, err := getRedisConfig()
	if err != nil {
		log.Fatal(err)
	}

	r.Use(sessions.Sessions("mySession", store))
	corsConfig := cors.DefaultConfig()
	corsConfig.AllowCredentials = true
	corsConfig.AllowOrigins = []string{"http://localhost:3000", "http://127.0.0.1:3000"}
	r.Use(cors.New(corsConfig))

	client, err := ent.Open("postgres", getDbConfig())
	if err != nil {
		log.Fatal(err)
	}
	defer client.Close()
	if err := client.Schema.Create(context.Background()); err != nil {
		log.Fatal(err)
	}

	v1 := r.Group("/api")
	{
		// Health
		v1.GET("/health", routes.Health)

		// User management
		v1.POST("/login", routes.Login(context.Background(), client))
		v1.POST("/logout", middlewares.Authentication(context.Background(), client), routes.Logout)
		v1.POST("/register", routes.Register(context.Background(), client))

		// Room management
		room := v1.Group("/room")
		{
			room.Use(middlewares.Authentication(context.Background(), client))
			room.GET("", routes.GetRoom(context.Background(), client))
			room.POST("", routes.CreateRoom(context.Background(), client))
			room.POST("/join", routes.Join(context.Background(), client))
			room.GET("/message", routes.GetRoomMessage(context.Background(), client))
			room.POST("/message", routes.PostRoomMessage(context.Background(), client))
			room.DELETE("/message", routes.DeleteRoomMessage(context.Background(), client))
			room.PUT("/message", routes.PutRoomMessage(context.Background(), client))
		}
	}

	_ = r.Run(":" + config.Config.Server.Port)
}
