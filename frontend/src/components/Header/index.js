import React from 'react';
import Helmet from 'react-helmet';

export default function Header() {
  return (
    <Helmet>
      <meta charSet="utf-8" />
      <title>Taqueria Bonjour</title>
      <link rel="canonical" href="http://bonjour.paulynomial.com/" />
    </Helmet>
  );
}
