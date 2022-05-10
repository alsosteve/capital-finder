# Python 401d1818
## Labs 16: Capital Finder
### Authors: Steve Ngo

## Overview
Deploy a serverless function to the cloud.

## Feature Tasks and Requirements
* Sign up with [Vercel](https://vercel.com/docs/get-started).
* Create a repository on Github and link it to Vercel account.
* Use [requests](https://docs.python-requests.org/en/latest/) library to interact with [REST Countries API](https://restcountries.com/#rest-countries)
* Create a serverless function following Vercel’s get-started directions that handles two kinds of queries:
  * The serverless function should handle a `GET` http request with a given country name that responds with a string with the form `The capital of X is Y`
    * E.g.`/capital-finder?country=Chile` should generate an http response of `The capital of Chile is Santiago`.
    * The serverless function should handle a `GET` http request with a given capital that responds with a string with the form `The capital of X is Y`
      * E.g.`/capital-finder?capital=Santiago` should generate an http response of `Santiago is the capital of Chile`.

## Stretch:
* Extend lab to take in country and capital at same time, then generate response informing user if the values supplied were a correct county/capital match.
* Handle the few countries with multiple capitals.
* Add currency, national languages, etc.

### Implementation Notes
* Vercel has a free plan. No credit card is required.
* The [Vercel CLI](https://vercel.com/docs/concepts/deployments/overview#vercel-cli) is useful (but not required) for local testing.

### User Acceptance Tests:
Project `README.md` should include working example urls for deployed function.

### Testing:
* []()