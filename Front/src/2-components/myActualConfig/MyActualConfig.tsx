import React, { useEffect, useState } from 'react';
import logo from './logo.svg';
import './MyActualConfig.css';
import { Container, Grid, Typography } from '@mui/material';
import { RecordButton } from '../RecordButton';
import { CommonButton } from '../CommonButton';
import { useDispatch, useSelector } from 'react-redux';
import { getRecordSettings, startRecord } from '../../4-redux/slices/mainSlice';
import { AppDispatch, store } from '../../4-redux/store';
import { RecordSettingsModel } from '../../5-crossCuttingConcerns/models/RecordSettingsModel';

function MyActualConfig() {
  let stateRecordSettings: RecordSettingsModel = useSelector((state:any) => state.main.recordSettings);
  const [formattedTime, setFormattedTime] = useState("00:00:00")

  useEffect(() => {
    const formatTime = () => {
      if (typeof stateRecordSettings.duration !== 'number' || isNaN(stateRecordSettings.duration)) {
        setFormattedTime("00:00:00");
        return;
      }
  
      let totalSeconds = stateRecordSettings.duration;
      let hours = Math.floor(totalSeconds / 3600);
      let minutes = Math.floor((totalSeconds - (hours * 3600)) / 60);
      let seconds = totalSeconds - (hours * 3600) - (minutes * 60);
  
      // Convertir a strings y asegurarse de que sean al menos 2 dígitos.
      let stringHours = hours.toString().padStart(2, '0');
      let stringMinutes = minutes.toString().padStart(2, '0');
      let stringSeconds = seconds.toString().padStart(2, '0');
  
      const currentFormattedTime = `${stringHours}:${stringMinutes}:${stringSeconds}`;
      setFormattedTime(currentFormattedTime);
    }
  
    formatTime();
  }, [stateRecordSettings]);

  return (
    <Container maxWidth="xl" sx={{
      display: 'flex',
      justifyContent: 'center',
      alignContent: 'center',
      py:4}}>
      <Grid container spacing={1} sx={{width: "100%", height: "auto"}}  >
         
         <Grid item xs={12}>
          <Typography className='config_title' variant="h6" component="h2">
            Tu configuracion actual:
          </Typography>
         </Grid>

         <Grid item xs={12}>
          <Typography className='config_label' variant="subtitle2" component="h2"
            sx={{ 
            display: 'inline',
            }}>
            Formato de video: 
              <Typography  variant="subtitle2" component="p"
                sx={{ 
                  display: 'inline',
                  }}
              > 
              { stateRecordSettings.video_format } 
              </Typography>
          </Typography>
         </Grid>
         

         <Grid item xs={12}>
          <Typography className='config_label' variant="subtitle2" component="h2"
            sx={{ 
            display: 'inline',
            }}>
            Tamaño de pantalla: <Typography  variant="subtitle2" component="p"
            sx={{ 
              display: 'inline',
              }}
              > { stateRecordSettings.screen_weight + 'x' + stateRecordSettings.screen_height } </Typography>
          </Typography>
         </Grid>
         

         <Grid item xs={12}>
          <Typography className='config_label' variant="subtitle2" component="h2"
            sx={{ 
            display: 'inline',
            }}>
            Cantidad de FPS: <Typography  variant="subtitle2" component="p"
            sx={{ 
              display: 'inline',
              }}
              > { stateRecordSettings.fps } </Typography>
          </Typography>
         </Grid>

         <Grid item xs={12}>
          <Typography className='config_label' variant="subtitle2" component="h2"
            sx={{ 
            display: 'inline',
            }}>
            Ruta de guardado: <Typography  variant="subtitle2" component="p"
            sx={{ 
              display: 'inline',
              }}
              > { stateRecordSettings.directory } </Typography>
          </Typography>
         </Grid>

         <Grid item xs={12}>
          <Typography className='config_label' variant="subtitle2" component="h2"
            sx={{ 
            display: 'inline',
            }}>
            Duracion: <Typography  variant="subtitle2" component="p"
            sx={{ 
              display: 'inline',
              }}
              > { formattedTime } </Typography>
          </Typography>
         </Grid>

      </Grid>
    </Container>
  );
}

export default MyActualConfig;
