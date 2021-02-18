package routes

import (
	"github.com/gin-gonic/gin"
	"net/http"
)

func Health(c *gin.Context) {
	c.String(http.StatusOK, "OK")
}
