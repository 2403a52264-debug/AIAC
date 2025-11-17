export type Item = {
  id: string;
  name: string;
  description: string;
  location: string;
  imageUrl: string;
  imageHint: string;
  dateFound: string;
  status: 'available' | 'claimed' | 'pending';
  claimedBy?: string; // User ID
  claimedDate?: string;
};

export type User = {
  id: string;
  name:string;
  email: string;
  role: 'student' | 'faculty' | 'admin';
};
