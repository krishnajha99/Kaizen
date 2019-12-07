const okta = require('@okta/okta-sdk-nodejs');

const client = new okta.Client({
  orgUrl: 'https://dev-705610.okta.com',
  token: '00-pWNs1MwxHtmWWZLIbHVA_oKlBsc7V36Nj9MRyZi'
});

module.exports = client;
