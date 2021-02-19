package middlewares

import (
	"context"
	"fmt"
	"github.com/gin-gonic/gin"
	"github.com/google/uuid"
	"go-message/ent"
	"net/http"
)

func Authentication(ctx context.Context, client *ent.Client) gin.HandlerFunc {
	return func(c *gin.Context) {
		cookie, err := c.Cookie("cookie")
		if err != nil {
			fmt.Println("Auth", err)
		}

		id, err := uuid.Parse(fmt.Sprintf("%v", cookie))
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
		c.Next()
	}
}
