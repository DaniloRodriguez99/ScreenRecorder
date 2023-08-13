import React, { useEffect, useState } from 'react';
import logo from './logo.svg';
import './RecordingSection.css';
import { Container, Grid, Typography } from '@mui/material';
import { RecordButton } from '../RecordButton';
import { CommonButton } from '../CommonButton';
import { useDispatch, useSelector } from 'react-redux';
import { cancelRecord, getRecordSettings, startRecord } from '../../4-redux/slices/mainSlice';
import { AppDispatch, store } from '../../4-redux/store';
import { RecordSettingsModel } from '../../5-crossCuttingConcerns/models/RecordSettingsModel';

function RecordingSection() {
  const dispatch = useDispatch();
  const dispatchThunk = useDispatch<AppDispatch>();

  let stateIsRecording = useSelector((state:any) => state.main.isRecording);
  let stateRecordSettings: RecordSettingsModel = useSelector((state:any) => state.main.recordSettings);

  const onRecord = () => {
    dispatchThunk(startRecord(stateRecordSettings));
  }

  const onCancelRecord = () => {
    dispatchThunk(cancelRecord());
  }

  return (
    <>
    {
      stateIsRecording ? <>
        <RecordButton onClick={onCancelRecord}> Detener Grabacion </RecordButton>
      </> :
      <>
        <RecordButton onClick={onRecord}> Grabar </RecordButton>
      </>
    }
    </>
  );
}

export default RecordingSection;
