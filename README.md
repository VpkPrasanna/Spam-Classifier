# Spam or Ham classifier Model 

## To reproduce the result 

- Just follow the notebook given under notebook section and follow the steps specified there.
---

# Tech Stack
> For Model : [Pytorch](https://pytorch.org/)

> For Creating Api - [FastApi](https://fastapi.tiangolo.com/)

> For Deployement - [Docker](https://www.docker.com/)
---
Which Model i have used ?
- Bert Model from [Hugging Face](https://huggingface.co/) 

---
How to Run the API ?

For that Build the docker file and run the docker file

Just Run 
- `docker-compose up`
## Note 
### Use  sudo before the docker command if it ask for root user permission. 
---

## To run the api without docker follow the below steps


- Run app.py file inside Src Folder.
- It will give us a URL where you can hit the api something like this `http://0.0.0.0:8000/` and route to `0.0.0.0:8000/docs`

## Reference Image
![Api UI](images/image1.png)

## Why i have note used Kubernetes ?
- The main reason is we dont have a bigger application where one micro service interact with other micro service.
- If we have a situation where we have a **Database** which stores all the response for each and every request,then that is where we can use multiple containers to run simultanously and scale up and down based on the needs of the application **demands.**
- That's Why i did not use any Kubernetes based approach to this solution.
---
# How a CI/CD pipeline works
![Api UI](images/cicd.png)
- This is how a typical CI/CD Pipeline works in an organisation.
- There are many tools to handle CI/CD Pipeline like 
1. Jenkins
2. Circle ci

> With Love VPK