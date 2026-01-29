import React, { useState, useEffect } from 'react';
import { Container, Typography, AppBar, Toolbar, Box } from '@mui/material';
import axios from 'axios';

function App() {
  return (
    <Box sx={{ flexGrow: 1 }}>
      <AppBar position="static" color="primary">
        <Toolbar>
          <Typography variant="h6" component="div">
            Nexus Industry Dashboard
          </Typography>
        </Toolbar>
      </AppBar>

      <Container sx={{ mt: 4 }}>
        <Typography variant="h4" gutterBottom>
          Monitoramento em Tempo Real
        </Typography>
        {/* Aqui entrarão nossos componentes de tabela e gráfico */}
        <Box sx={{ p: 3, bgcolor: '#f5f5f5', borderRadius: 2 }}>
          Status do Sistema: Conectando à API...
        </Box>
      </Container>
    </Box>
  );
}

export default App;