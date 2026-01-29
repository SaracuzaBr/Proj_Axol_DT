import React, { useState, useEffect } from 'react';
import { Container, Typography, AppBar, Toolbar, Box, Table, TableBody, TableCell, TableHead, TableRow, Paper } from '@mui/material';
import axios from 'axios';

function App() {
  const [readings, setReadings] = useState([]);

  const fetchData = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:8000/readings');
      setReadings(response.data);
    } catch (error) {
      print("Erro ao buscar dados:", error);
    }
  };

  // Busca dados ao carregar e define um intervalo de 3 segundos
  useEffect(() => {
    fetchData();
    const interval = setInterval(fetchData, 3000);
    return () => clearInterval(interval);
  }, []);

  return (
    <Box sx={{ flexGrow: 1 }}>
      <AppBar position="static"><Toolbar><Typography variant="h6">Nexus Industry</Typography></Toolbar></AppBar>
      <Container sx={{ mt: 4 }}>
        <Typography variant="h4" gutterBottom>Monitoramento em Tempo Real</Typography>
        <Paper elevation={3}>
          <Table>
            <TableHead>
              <TableRow>
                <TableCell>Máquina</TableCell>
                <TableCell>Temperatura (°C)</TableCell>
                <TableCell>Vibração (mm/s)</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {readings.map((r) => (
                <TableRow key={r.id}>
                  <TableCell>{r.machine_id}</TableCell>
                  <TableCell>{r.temperature}</TableCell>
                  <TableCell>{r.vibration}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </Paper>
      </Container>
    </Box>
  );
}

export default App;