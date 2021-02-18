package middlewares

import (
	"context"
	"fmt"
	"github.com/gin-contrib/sessions"
	"github.com/gin-gonic/gin"
	"github.com/google/uuid"
	"go-message/ent"
	"net/http"
)

func Authentication(ctx context.Context, client *ent.Client) gin.HandlerFunc {
	return func(c *gin.Context) {
		session := sessions.Default(c)
		sessionId := session.Get("Id")

		if sessionId == nil {
			c.String(http.StatusUnauthorized, "Unauthorized")
			c.Abort()
			return
		}

		id, err := uuid.Parse(fmt.Sprintf("%v", sessionId))
		if err != nil {
			c.String(http.StatusUnauthorized, "Invalid uuid")
			c.Abort()
			return
		}

		user, err := client.User.Get(ctx, id)
		if err != nil {
			c.String(http.StatusNotFound, "User not found")
			c.Abort()
			return
		}
		c.Request = c.Request.WithContext(context.WithValue(c.Request.Context(), "userID", user.ID))
	}
}
