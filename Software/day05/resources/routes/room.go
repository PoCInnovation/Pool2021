package routes

import (
	"context"
	"github.com/gin-gonic/gin"
	"go-message/ent"
	"net/http"
)

// createRoom POST -> Create room (must be login)
func CreateRoom(ctx context.Context, client *ent.Client) gin.HandlerFunc {
	fn := func(c *gin.Context) {
		newRoom, err := client.Room.
			Create().
			Save(ctx)
		if err != nil {
			c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
			return
		}
		c.JSON(http.StatusCreated, gin.H{"room": newRoom})
	}
	return gin.HandlerFunc(fn)
}

// getRoom GET -> Return the list of available rooms
func GetRoom(ctx context.Context, client *ent.Client) gin.HandlerFunc {
	fn := func(c *gin.Context) {
		rooms, err := client.Room.
			Query().
			All(ctx)
		if err != nil {
			c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
			return
		}
		c.JSON(http.StatusOK, gin.H{"rooms": rooms})
	}
	return gin.HandlerFunc(fn)
}
