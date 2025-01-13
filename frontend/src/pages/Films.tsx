import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import {
  Container,
  Grid,
  Card,
  CardContent,
  CardMedia,
  Typography,
  Rating,
  Box,
  AppBar,
  Toolbar,
  Button,
  TextField,
} from '@mui/material';
import { useDispatch } from 'react-redux';
import { filmsApi } from '../services/api';
import { logout } from '../store/slices/authSlice';

interface Film {
  id: number;
  name: string;
  description: string;
  genre: string;
  image_url: string;
  average_rating: number;
}

const Films: React.FC = () => {
  const navigate = useNavigate();
  const dispatch = useDispatch();
  const [films, setFilms] = useState<Film[]>([]);
  const [searchQuery, setSearchQuery] = useState('');

  useEffect(() => {
    fetchFilms();
  }, []);

  const fetchFilms = async () => {
    try {
      const response = await filmsApi.getFilms();
      setFilms(response.data);
    } catch (err) {
      // If unauthorized, redirect to login
      if ((err as any)?.response?.status === 401) {
        navigate('/login');
      }
    }
  };

  const handleLogout = () => {
    dispatch(logout());
    navigate('/login');
  };

  const filteredFilms = films.filter((film) =>
    film.name.toLowerCase().includes(searchQuery.toLowerCase())
  );

  return (
    <Box sx={{ flexGrow: 1 }}>
      <AppBar position="static">
        <Toolbar>
          <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
            Filmers
          </Typography>
          <Button color="inherit" onClick={handleLogout}>
            Logout
          </Button>
        </Toolbar>
      </AppBar>
      <Container sx={{ mt: 4 }}>
        <TextField
          fullWidth
          label="Search Films"
          variant="outlined"
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
          sx={{ mb: 4 }}
        />
        <Grid container spacing={4}>
          {filteredFilms.map((film) => (
            <Grid item key={film.id} xs={12} sm={6} md={4}>
              <Card sx={{ height: '100%', display: 'flex', flexDirection: 'column' }}>
                <CardMedia
                  component="img"
                  height="200"
                  image={film.image_url ? `http://127.0.0.1:8000${film.image_url}` : 'https://via.placeholder.com/300x200'}
                  alt={film.name}
                  sx={{ 
                    objectFit: 'cover',
                    height: 200,
                    width: '100%'
                  }}
                  onError={(e) => {
                    const target = e.target as HTMLImageElement;
                    target.src = 'https://via.placeholder.com/300x200';
                  }}
                />
                <CardContent sx={{ flexGrow: 1 }}>
                  <Typography gutterBottom variant="h5" component="h2">
                    {film.name}
                  </Typography>
                  <Typography color="text.secondary" paragraph>
                    {film.description}
                  </Typography>
                  <Typography color="text.secondary" gutterBottom>
                    Genre: {film.genre}
                  </Typography>
                  <Box sx={{ display: 'flex', alignItems: 'center' }}>
                    <Rating value={film.average_rating || 0} readOnly precision={0.5} />
                    <Typography sx={{ ml: 1 }}>
                      {film.average_rating ? `(${film.average_rating.toFixed(1)})` : '(No ratings yet)'}
                    </Typography>
                  </Box>
                </CardContent>
              </Card>
            </Grid>
          ))}
        </Grid>
      </Container>
    </Box>
  );
};

export default Films; 