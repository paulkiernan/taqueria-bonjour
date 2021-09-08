import React from 'react';

import 'react-phone-input-2/lib/material.css';
import 'yup-phone';
import * as Yup from 'yup';
import Alert from '@material-ui/lab/Alert';
import Button from '@material-ui/core/Button';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';
import PhoneInput from 'react-phone-input-2';
import TextField from '@material-ui/core/TextField';
import Typography from '@material-ui/core/Typography';
import { Formik } from 'formik';

import { Event, Exception } from '../Tracking';

const SignupSchema = Yup.object().shape({
  name: Yup.string()
    .min(2, 'Name too short!')
    .max(64, 'Name too long!')
    .required('Required'),
  number: Yup.string()
    .phone()
    .required('Required'),
});

export default function SubscribeDialog() {
  // const apiEndpoint = "http://localhost:8080"
  // const apiEndpoint = process.env.REACT_APP_BACKEND_API_URL;
  const apiEndpoint = "api"

  const [open, setOpen] = React.useState(false);

  const handleClickOpen = () => {
    Event('SUBSCRIBE', 'open', 'SubscribeDialog');
    setOpen(true);
  };

  const handleClose = () => {
    Event('SUBSCRIBE', 'close', 'SubscribeDialog');
    setOpen(false);
  };

  const submitApiRequest = (values, actions) => {
    Event('SUBSCRIBE', 'submit', 'SubscribeDialog');

    const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        name: values.name,
        number: values.number,
        code: values.countryCode,
      }),
    };
    fetch(`${apiEndpoint}/add`, requestOptions)
      .then(async (response) => {
        const data = await response.json();

        // check for error response
        if (!response.ok) {
          // get error message from body or default to response status
          const error = (data && data.message) || response.status;
          actions.setStatus([data.status, data.message]);
          Exception(data.message, false);
          return Promise.reject(error);
        }

        actions.setStatus([data.status, data.message]);
        actions.setSubmitting(false);
        return 'Success';
      })
      .catch((error) => {
        actions.setStatus(['error', 'Error submitting information to server!']);
        Exception(error, true);
        actions.setSubmitting(false);
      });
  };

  return (
    <div>
      <Button color="primary" onClick={handleClickOpen}>
        <Typography
          variant="button"
          gutterBottom
          style={{
            fontFamily: 'PermanentMarker',
          }}
        >
          alerte moi
        </Typography>
      </Button>
      <Dialog
        open={open}
        onClose={handleClose}
        aria-labelledby="form-dialog-title"
      >

        <DialogTitle id="form-dialog-title">Bonjour!</DialogTitle>

        <DialogContent>

          <DialogContentText>
            To join the Rapid Response Team® please enter your name and phone
            number here.
          </DialogContentText>
          <DialogContentText>
            We will send alerts erratically.
          </DialogContentText>

          <Formik
            initialValues={{
              name: '',
              number: '',
              countryCode: '',
              countryDialCode: '',
              countryName: '',
            }}
            validationSchema={SignupSchema}
            onSubmit={submitApiRequest}
          >
            {({
              errors,
              touched,
              values,
              handleSubmit,
              handleChange,
              isSubmitting,
              status,
            }) => (
              <form onSubmit={handleSubmit}>
                {
                  status ? (
                    <Alert severity={status[0]}>
                      {status[1]}
                    </Alert>
                  ) : null
                }
                {
                  errors.number && touched.number ? (
                    <Alert severity="error">
                      {errors.number}
                    </Alert>
                  ) : null
                }
                <TextField
                  required
                  autoFocus
                  margin="dense"
                  id="name"
                  label="Name"
                  type="name"
                  onChange={handleChange}
                  value={values.name}
                  style={{
                    marginBottom: 15,
                  }}
                />
                <PhoneInput
                  required
                  rargin="dense"
                  id="number"
                  label="Phone"
                  country="us"
                  value={values.number}
                  onChange={(number, country) => {
                    /* eslint-disable no-param-reassign */
                    values.number = `+${number}`;
                    values.countryCode = country.countryCode;
                    values.countryDialCode = country.dialCode;
                    values.countryName = country.name;
                    /* eslint-enable no-param-reassign */
                  }}
                />
                <DialogActions>
                  <Button onClick={handleClose} color="primary">
                    Cancel
                  </Button>
                  <Button color="primary" type="submit" disabled={isSubmitting}>
                    Subscribe
                  </Button>
                </DialogActions>
              </form>
            )}
          </Formik>

        </DialogContent>
      </Dialog>
    </div>
  );
}
