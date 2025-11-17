import type { Item, User } from './definitions';

export const items: Item[] = [];

export const users: User[] = [
  { id: 'user-1', name: 'Admin User', email: 'admin@sru.edu', role: 'admin' },
  { id: 'user-2', name: 'Faculty Member', email: 'faculty@sru.edu', role: 'faculty' },
  { id: 'user-3', name: 'Student User', email: 'student@sru.edu', role: 'student' },
];

export const campusLocations = [
    'Library',
    'Cafeteria',
    'Student Union',
    'Main Quad',
    'Gymnasium',
    'Lecture Hall A',
    'Lecture Hall B',
    'Lecture Hall C1',
    'Campus Pond',
    'Admin Building',
    'Parking Lot A',
    'Parking Lot B',
];
