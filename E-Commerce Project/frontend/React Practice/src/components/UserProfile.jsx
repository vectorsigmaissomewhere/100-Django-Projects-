import React from 'react';
import { Box, CssBaseline, Drawer as MuiDrawer, List, ListItem, ListItemIcon, ListItemText, Typography, IconButton } from '@mui/material';
import { styled } from '@mui/system';
import AccountCircleIcon from '@mui/icons-material/AccountCircle';
import SettingsIcon from '@mui/icons-material/Settings';
import LogoutIcon from '@mui/icons-material/Logout';
import HomeIcon from '@mui/icons-material/Home';
import MenuIcon from '@mui/icons-material/Menu';

// Define styles using `styled` from @mui/system
const drawerWidth = 240;

const Root = styled('div')(({ theme }) => ({
  display: 'flex',
}));

const AppBar = styled('div')(({ theme }) => ({
  zIndex: theme.zIndex.drawer + 1,
}));

const Drawer = styled(MuiDrawer)(({ theme }) => ({
  width: drawerWidth,
  flexShrink: 0,
  '& .MuiDrawer-paper': {
    width: drawerWidth,
  },
}));

const Content = styled(Box)(({ theme }) => ({
  flexGrow: 1,
  padding: theme.spacing(3),
}));

const Toolbar = styled('div')(({ theme }) => theme.mixins.toolbar);

const MenuButton = styled(IconButton)(({ theme }) => ({
  marginRight: theme.spacing(2),
  display: 'none',
  [theme.breakpoints.down('sm')]: {
    display: 'block',
  },
}));

const Dashboard = () => {
  const [mobileOpen, setMobileOpen] = React.useState(false);

  const handleDrawerToggle = () => {
    setMobileOpen(!mobileOpen);
  };

  const drawer = (
    <div>
      <Toolbar />
      <List>
        {['Home', 'Profile', 'Settings', 'Logout'].map((text, index) => (
          <ListItem button key={text}>
            <ListItemIcon>
              {index === 0 ? <HomeIcon /> : null}
              {index === 1 ? <AccountCircleIcon /> : null}
              {index === 2 ? <SettingsIcon /> : null}
              {index === 3 ? <LogoutIcon /> : null}
            </ListItemIcon>
            <ListItemText primary={text} />
          </ListItem>
        ))}
      </List>
    </div>
  );

  return (
    <Root>
      <CssBaseline />
      <MenuButton
        color="inherit"
        aria-label="open drawer"
        edge="start"
        onClick={handleDrawerToggle}
      >
        <MenuIcon />
      </MenuButton>
      <Drawer
        variant="permanent"
        open
      >
        {drawer}
      </Drawer>
      <Drawer
        variant="temporary"
        open={mobileOpen}
        onClose={handleDrawerToggle}
        ModalProps={{
          keepMounted: true, // Better open performance on mobile.
        }}
      >
        {drawer}
      </Drawer>
      <Content component="main">
        <Toolbar />
        <Typography variant="h4">Dashboard</Typography>
        <Typography paragraph>
          This is the main content area. Here you can display the details of the selected section.
        </Typography>
      </Content>
    </Root>
  );
};

export default Dashboard;