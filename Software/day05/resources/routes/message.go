package routes

import (
	"context"
	"github.com/gin-gonic/gin"
	"github.com/google/uuid"
	"go-message/ent"
	"go-message/ent/message"
	"go-message/ent/room"
	"net/http"
)

// roomMessage GET {roomId: X} -> Return list of message from roomID
func GetRoomMessage(ctx context.Context, client *ent.Client) gin.HandlerFunc {
	type roomMessage struct {
		RoomID string `form:"roomID" binding:"required"`
	}

	fn := func(c *gin.Context) {
		var data roomMessage
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

		messages, err := rooms.QueryMessages().WithUser().All(ctx)
		if err != nil {
			c.JSON(http.StatusNotFound, gin.H{"error": err.Error()})
			return
		}
		c.JSON(http.StatusOK, gin.H{"Messages": messages})
	}
	return fn
}

// roomMessage POST {roomId : X} -> Add a message to roomID
func PostRoomMessage(ctx context.Context, client *ent.Client) gin.HandlerFunc {
	type roomMessageQuery struct {
		RoomID string `form:"roomID" binding:"required"`
	}

	type roomMessageBody struct {
		Message string `json:"message" binding:"required"`
	}

	fn := func(c *gin.Context) {
		var dataQuery roomMessageQuery
		var dataBody roomMessageBody

		if err := c.ShouldBindQuery(&dataQuery); err != nil {
			c.JSON(http.StatusBadRequest, gin.H{"error_parsing": err.Error()})
			return
		}

		roomID, err := uuid.Parse(dataQuery.RoomID)
		if err != nil {
			c.JSON(http.StatusBadRequest, gin.H{"error_parsing": err.Error()})
			return
		}

		if err := c.ShouldBindJSON(&dataBody); err != nil {
			c.JSON(http.StatusBadRequest, gin.H{"error_parsing": err.Error()})
			return
		}

		userID := c.Request.Context().Value("userID").(uuid.UUID)
		userEntity, err := client.User.Get(ctx, userID)
		if err != nil {
			c.JSON(http.StatusNotFound, gin.H{"error_search": err.Error()})
			return
		}

		newMessage, err := client.Message.
			Create().
			SetMessage(dataBody.Message).
			SetUser(userEntity).
			Save(ctx)
		if err != nil {
			c.JSON(http.StatusInternalServerError, gin.H{"error_message": err.Error()})
			return
		}

		_, err = client.Room.Update().
			Where(room.ID(roomID)).
			AddMessages(newMessage).
			Save(ctx)
		if err != nil {
			c.JSON(http.StatusInternalServerError, gin.H{"error_room": err.Error()})
			return
		}

		c.String(http.StatusCreated, "Message created !")
	}
	return fn
}

// roomMessage Delete {roomId: X, messageId: X} -> Delete a message from roomID (check if sender has the good ID)
func DeleteRoomMessage(ctx context.Context, client *ent.Client) gin.HandlerFunc {
	type roomMessage struct {
		RoomID    string `form:"roomID" binding:"required"`
		MessageID string `form:"messageID" binding:"required"`
	}

	fn := func(c *gin.Context) {
		var data roomMessage

		if err := c.ShouldBindQuery(&data); err != nil {
			c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
			return
		}

		roomID, err := uuid.Parse(data.RoomID)
		if err != nil {
			c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
			return
		}

		_, err = client.Room.Get(ctx, roomID)
		if err != nil {
			c.JSON(http.StatusNotFound, gin.H{"error": err.Error()})
			return
		}

		messageID, err := uuid.Parse(data.MessageID)
		if err != nil {
			c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
			return
		}
		err = client.Message.DeleteOneID(messageID).Exec(ctx)
		if err != nil {
			c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
			return
		}

		c.String(http.StatusOK, "Message deleted")
	}
	return fn
}

// roomMessage PUT {room:Id: X, messageId: X} -> Update a message from roomID
func PutRoomMessage(ctx context.Context, client *ent.Client) gin.HandlerFunc {
	type roomMessageQuery struct {
		RoomID    string `form:"roomID" binding:"required"`
		MessageID string `form:"messageID" binding:"required"`
	}

	type roomMessageBody struct {
		Message string `json:"message" binding:"required"`
	}

	fn := func(c *gin.Context) {
		var dataQuery roomMessageQuery
		var dataBody roomMessageBody

		if err := c.ShouldBindQuery(&dataQuery); err != nil {
			c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
			return
		}

		messageID, err := uuid.Parse(dataQuery.MessageID)
		if err != nil {
			c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
			return
		}

		if err := c.ShouldBindJSON(&dataBody); err != nil {
			c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
			return
		}

		_, err = client.Message.
			Update().
			Where(message.ID(messageID)).
			SetMessage(dataBody.Message).
			Save(ctx)
		if err != nil {
			c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
			return
		}
		c.String(http.StatusOK, "Message updated")
	}
	return fn
}
