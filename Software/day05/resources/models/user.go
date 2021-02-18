package models

import (
	"context"
	"errors"
	"go-message/ent"
	"go-message/ent/user"
)

type User struct {
	Username       string `json:"username" binding:"required"`
	Password       string `json:"password" binding:"required"`
	ProfilePicture string `json:"profilePicture" binding:"required"`
}

func CreateUser(ctx context.Context, client *ent.Client, userDTO User) (*ent.User, error) {
	newUser, err := client.User.
		Create().
		SetUsername(userDTO.Username).
		SetPassword(userDTO.Password).
		SetProfilePicture(userDTO.ProfilePicture).
		Save(ctx)
	if err != nil {
		return nil, err
	}
	return newUser, nil
}

type Credential struct {
	Username string `json:"username" binding:"required"`
	Password string `json:"password" binding:"required"`
}

func GetUser(ctx context.Context, client *ent.Client, userCredential Credential) (*ent.User, error) {
	users, err := client.User.Query().
		Where(
			user.Username(userCredential.Username),
			user.Password(userCredential.Password)).
		All(ctx)
	if err != nil {
		return nil, err
	}
	if len(users) == 0 {
		return nil, errors.New("user not found")
	}
	return users[0], nil
}
