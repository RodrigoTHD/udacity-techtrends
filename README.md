# Techtrends app

## Available Scripts

In the project directory, you can run:


### Build

Docker command used to build the application.

```cmd
docker build -t techtrends .
```

### Run

Docker command used to run the application with port `7111`.

```cmd
docker run --name techtrends -d -p 7111:3111 techtrends
```

### Logs

Docker command used to get the application logs.

```cmd
docker logs techtrends
```
### Launch

After execute the run command. open the application at the address [http://127.0.0.1:7111](http://127.0.0.1:7111) in the browser.

