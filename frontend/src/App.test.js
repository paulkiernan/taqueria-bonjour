import React from 'react';

import { render, screen } from '@testing-library/react';
import App from './App';

test('renders index text', () => {
  render(<App />);
  const linkElement = screen.getByText(/a forthcoming radical new concept in food/i);
  expect(linkElement).toBeInTheDocument();
});

test('renders alert link', () => {
  render(<App />);
  const linkElement = screen.getByText(/alerte moi/i);
  expect(linkElement).toBeInTheDocument();
});
