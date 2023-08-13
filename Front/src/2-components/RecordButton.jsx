
import { styled } from '@mui/material/styles';
import Button, { ButtonProps } from '@mui/material/Button';

const RecordButton = styled(Button)({
    height: '100px',
    width: '100%',
    boxShadow: 'none',
    textTransform: 'none',
    fontSize: 16,
    padding: '6px 12px',
    border: '1px solid',
    lineHeight: 1.5,
    backgroundColor: '#e22431',
    borderColor: '#d1212d',
    color: '#fff',
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
      backgroundColor: '#d1212d',
      borderColor: '#d1212d',
      boxShadow: 'none',
    },
    '&:active': {
      boxShadow: 'none',
      backgroundColor: '#d1212d',
      borderColor: '#d1212d',
    },
    '&:focus': {
      boxShadow: '0 0 0 0.2rem rgb(252, 45, 76, .5)',
    },
  });

  export { RecordButton };