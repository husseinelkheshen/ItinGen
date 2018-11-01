# ItinGen

ItinGen is a web based application that allows users to randomly
generate optimized itineraries for their schedules to explore a new city
or rediscover a city they have been living in for years

## Dependecies
### Homebrew
```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
### Node.js / NPM
```bash
brew install node
```

### Java JDK for E2E Testing (Selenium Server)
```bash
brew cask install java
```

## Build Setup

``` bash
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report

# run unit tests
npm run unit

# run e2e tests
npm run e2e

# run all tests
npm test
```

Yarn can also be used instead of npm. Examples:

```bash
# install dependecies
yarn install

# serve with hor reload at localhost:8080
yarn start

# run unit tests
yarn test

# run linter
yarn lint
```


For a detailed explanation on how things work, check out the [guide](http://vuejs-templates.github.io/webpack/) and [docs for vue-loader](http://vuejs.github.io/vue-loader).
