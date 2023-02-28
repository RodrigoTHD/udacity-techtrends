# Techtrends app

### Build
```cmd
docker build ./ -t techtrends
```

### Start

Run the command below to start the application with 

```cmd
docker container run  -d -p 3111:3111 techtrends
```


# Available Scripts

In the project directory, you can run:

## Build

Build the container with tag name `techtrends`.

```cmd
docker build ./ -t techtrends
```

## Launch

Runs the app in the development mode.

```cmd
docker container run  -d -p 3111:3111 techtrends
```

Open the application at the address [http://127.0.0.1:3111](http://127.0.0.1:3111) in the browser.

