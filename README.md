# Techtrends

The web application is written using the Python Flask framework. It uses SQLite, a lightweight disk-based database to store the submitted articles.

TechTrends is an online website used as a news sharing platform, that enables consumers to access the latest news within the cloud-native ecosystem. In addition to accessing the available articles, readers are able to create new media articles and share them.

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

