package routes

import (
	"context"
	"fmt"
	"github.com/gin-contrib/sessions"
	"github.com/gin-gonic/gin"
	"github.com/google/uuid"
	"go-message/ent"
	"go-message/models"
	"net/http"
)

// createAccount POST {username: X, password: X, profilePicture: X} -> Create account and set cookie
func Register(ctx context.Context, client *ent.Client) gin.HandlerFunc {
	fn := func(c *gin.Context) {
		var data models.User

		if err := c.ShouldBindJSON(&data); err != nil {
			fmt.Println(err)
			c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
			return
		}

		newUser, err := models.CreateUser(ctx, client, data)
		if err != nil {
			fmt.Println(err)
			c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
			return
		}
		c.JSON(http.StatusOK, gin.H{"User created": newUser})
	}
	return fn
}

// login POST {username: X, password: X} -> Create cookie
func Login(ctx context.Context, client *ent.Client) gin.HandlerFunc {
	fn := func(c *gin.Context) {
		var data models.Credential

		if err := c.ShouldBindJSON(&data); err != nil {
			fmt.Println(err)
			c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
			return
		}

		user, err := models.GetUser(ctx, client, data)
		if err != nil {
			c.JSON(http.StatusNotFound, gin.H{"error": err.Error()})
			return
		}
		c.SetCookie("cookie", user.ID.String(), 3600, "/", "127.0.0.1", false, true)
		//	session := sessions.Default(c)
	//	session.Set("Id", user.ID.String())
	//	err = session.Save()
	//	if err != nil {
	//		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
	//		return
	//	}

		c.String(http.StatusOK, "User sign in successfully")
	}
	return fn
}

func Logout(c *gin.Context) {
	session := sessions.Default(c)
	session.Clear()
	_ = session.Save()

	c.String(http.StatusOK, "User sign out successfully")
}

// join POST {roomId: X} -> Check if roomID exist (must be login)
func Join(ctx context.Context, client *ent.Client) gin.HandlerFunc {
	type join struct {
		RoomID string `form:"roomID" binding:"required"`
	}

	fn := func(c *gin.Context) {
		var data join

		if err := c.ShouldBindQuery(&data); err != nil {
			c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
			return
		}

		roomID, err := uuid.Parse(data.RoomID)
		if err != nil {
			c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
			return
		}

		rooms, err := client.Room.Get(ctx, roomID)
		if err != nil {
			c.JSON(http.StatusNotFound, gin.H{"error": err.Error()})
			return
		}
		c.JSON(http.StatusOK, gin.H{"Room to join": rooms.ID})
	}
	return fn
}
