import React, { useEffect, useState } from 'react';
import logo from './logo.svg';
import './ConfigurationPage.css';
import { Container, Grid, MenuItem, TextField } from '@mui/material';
import { RecordButton } from '../../2-components/RecordButton';
import { CommonButton } from '../../2-components/CommonButton';
import { useDispatch, useSelector } from 'react-redux';
import { AppDispatch, store } from '../../4-redux/store';
import MyActualConfig from '../../2-components/myActualConfig/MyActualConfig';
import RecordingSection from '../../2-components/recordingSection/RecordingSection';
import { VideoFormatsService } from '../../3-services/VideoService';
import { getRecordSettings } from '../../4-redux/slices/mainSlice';
import { RecordSettingsModel } from '../../5-crossCuttingConcerns/models/RecordSettingsModel';
import DirectoryPicker from '../../2-components/DirectoryPicker';

function ConfigurationPage() {
  const dispatch = useDispatch();
  const dispatchThunk = useDispatch<AppDispatch>();
  const videoFormats = VideoFormatsService.getAllVideoFormats();

  const getMenuItemValues = () => {
    let menuItems = videoFormats.map(({key, value}) => {
      return {
        value: value,
        label: key
      }
    })

    return menuItems;
  }

  let currentSettings: RecordSettingsModel = useSelector((state: any) => state.main.recordSettings)


  return (
    <Container maxWidth="xl" sx={{
      display: 'flex',
      justifyContent: 'center',
      alignContent: 'center',
      width: "100vw", 
      height: "100vh"}}>
      <Grid container spacing={2} sx={{width: "100%", height: "100%", py: 3 }}  >
         
         <Grid item sx={{ py: 3 }}>
          <TextField
            id="outlined-select-currency"
            select
            label="Formato de video"
            defaultValue={currentSettings.video_format as Number}
            helperText="Please select a video format "
          >
            {getMenuItemValues().map((option) => (
              <MenuItem key={option.value} value={option.value}>
                {option.label}
              </MenuItem>
            ))}
          </TextField>
         </Grid>

         <Grid item>
          <DirectoryPicker></DirectoryPicker>
         </Grid>
      </Grid>
    </Container>
  );
}

export default ConfigurationPage;
