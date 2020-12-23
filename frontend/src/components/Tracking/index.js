import ReactGA from 'react-ga';

export const initGA = (trackingID) => {
  ReactGA.initialize(trackingID, {
    debug: (process.env.REACT_APP_GOOGLE_ANALYTICS_ENABLE_DEBUG === 'true'),
  });
};

export const PageView = () => {
  ReactGA.pageview(
    window.location.pathname + window.location.search,
  );
};

export const Event = (category: string, action: string, label: string) => {
  ReactGA.event({
    category,
    action,
    label,
  });
};

export const Exception = (description: string, fatal: boolean) => {
  ReactGA.exception({
    description,
    fatal,
  });
};
