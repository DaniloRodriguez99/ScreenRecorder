import React, { useEffect } from 'react';
import logo from './logo.svg';
import './App.css';
import { Provider, useDispatch } from 'react-redux';
import { getRecordSettings, initializeSocket } from './4-redux/slices/mainSlice';
import { AppDispatch, store } from './4-redux/store';
import { RouterProvider, createBrowserRouter } from 'react-router-dom';
import MainPage from './1-pages/mainPage/MainPage';
import ConfigurationPage from './1-pages/configurationPage/ConfigurationPage';

const router = createBrowserRouter([
  {
    path: "/",
    element: <MainPage />,
  },
  {
    path: "/configuration",
    element: <ConfigurationPage />,
  },
]);

function App() {
  const dispatchThunk = useDispatch<AppDispatch>();

    useEffect(() => {
      dispatchThunk(initializeSocket());
      dispatchThunk(getRecordSettings());
    }, [dispatchThunk]);

    
  return (
    <RouterProvider router={router} />
  );
}

export default App;
