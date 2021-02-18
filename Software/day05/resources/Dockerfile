FROM golang:1.15-alpine as build

WORKDIR /app

COPY . .

RUN mkdir /build

RUN go build -o /build/ .

FROM alpine as binary

COPY --from=build /build/go-message .

ENTRYPOINT ["./go-message"]
