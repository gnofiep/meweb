import { Typography, Button } from "@mui/material";

export default function Home() {
  return (
    <div>
      <Typography variant="h3">Hi, I'm Ash</Typography>
      <Typography>Full-stack developer specializing in React & AI</Typography>
      <Button variant="contained" href="/projects">View My Projects</Button>
    </div>
  );
}