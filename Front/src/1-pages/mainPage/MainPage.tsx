import React, { useEffect, useState } from 'react';
import logo from './logo.svg';
import './MainPage.css';
import { Container, Grid } from '@mui/material';
import { RecordButton } from '../../2-components/RecordButton';
import { CommonButton } from '../../2-components/CommonButton';
import { useDispatch, useSelector } from 'react-redux';
import { AppDispatch, store } from '../../4-redux/store';
import MyActualConfig from '../../2-components/myActualConfig/MyActualConfig';
import RecordingSection from '../../2-components/recordingSection/RecordingSection';
import { useNavigate } from 'react-router-dom';

function MainPage() {
  const dispatch = useDispatch();
  const dispatchThunk = useDispatch<AppDispatch>();
  const navigate = useNavigate();


  let stateIsRecording = useSelector((state:any) => state.main.isRecording);
  let stateRecordSettings = useSelector((state:any) => state.main.recordSettings);

  const onConfiguration = () => {
    navigate('/configuration')
  }

  const onScheduleRecord = () => {
    
  }

  return (
    <Container maxWidth="xl" sx={{
      display: 'flex',
      justifyContent: 'center',
      alignContent: 'center',
      width: "100vw", 
      height: "100vh"}}>
      <Grid container spacing={2} sx={{width: "100%", height: "100%"}}  >
         
          <Grid item xs={6} sx={{
            display: 'flex',
            flexDirection: 'column',
            alignContent: 'center',
            justifyContent: 'space-evenly'

          }}>
            
            <CommonButton onClick={onConfiguration}> Configuracion </CommonButton>

            <CommonButton onClick={onScheduleRecord}> Programar Grabacion </CommonButton>

            <RecordingSection />

          </Grid>

          <Grid item xs={6}>
            
            <MyActualConfig />

          </Grid>


      </Grid>
    </Container>
  );
}

export default MainPage;
