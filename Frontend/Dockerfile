FROM node:16-alpine as build

ARG VITE_API_URL
ENV VITE_API_URL=$VITE_API_URL

RUN apk update && apk upgrade && \
  apk add --no-cache bash git openssh

RUN mkdir /app

WORKDIR /app

COPY package.json .

RUN npm install

COPY . .

RUN npm run build

# ---------------

FROM node:16-alpine

RUN mkdir -p /app/dist

WORKDIR /app

COPY --from=build /app/dist ./dist
COPY --from=build /app/package.json .
COPY --from=build /app/web-server.js .

ENV NODE_ENV production

RUN npm install --production

EXPOSE 3000

CMD ["node", "web-server.js"]
