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

## Build the docker file 
`sudo docker build --tag <Name for the docker image> .`

Example
 - `docker build --tag spam-model .`

## Run the docker container
`sudo docker --publish <Mapping port> <Name for the docker>`

Example

- `docker --publish 8000:8000 spam-model`

## Note 
### Use  sudo before the docker command if it ask for root user permission. 
---