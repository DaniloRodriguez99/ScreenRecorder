
import { styled } from '@mui/material/styles';
import Button, { ButtonProps } from '@mui/material/Button';

const CommonButton = styled(Button)({
    width: '100%',
    boxShadow: 'none',
    textTransform: 'none',
    fontSize: 16,
    padding: '6px 12px',
    border: '1px solid',
    lineHeight: 1.5,
    backgroundColor: 'rgb(232, 232, 232)',
    borderColor: 'rgb(66, 66, 66)',
    color: 'rgb(96, 96, 96)',
    fontFamily: [
      '-apple-system',
      'BlinkMacSystemFont',
      '"Segoe UI"',
      'Roboto',
      '"Helvetica Neue"',
      'Arial',
      'sans-serif',
      '"Apple Color Emoji"',
      '"Segoe UI Emoji"',
      '"Segoe UI Symbol"',
    ].join(','),
    '&:hover': {
      backgroundColor: 'rgb(204, 204, 204)',
      borderColor: 'rgb(66, 66, 66)',
      boxShadow: 'none',
    },
    '&:active': {
      boxShadow: 'none',
      backgroundColor: 'rgb(204, 204, 204)',
    },
    '&:focus': {
      boxShadow: '0 0 0 0.2rem rgb(204, 204, 204, .5)',
    },
  });

  export { CommonButton };