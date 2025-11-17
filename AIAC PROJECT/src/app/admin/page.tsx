import { items, users } from '@/lib/data';
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from '@/components/ui/table';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import type { Item } from '@/lib/definitions';

const getStatusBadge = (status: Item['status']) => {
    switch (status) {
      case 'available':
        return <Badge variant="secondary" className="bg-green-200 text-green-900">Available</Badge>;
      case 'claimed':
        return <Badge variant="destructive">Claimed</Badge>;
      case 'pending':
        return <Badge variant="outline" className="bg-yellow-200 text-yellow-900 border-yellow-300">Pending</Badge>;
    }
  };

export default function AdminPage() {
  return (
    <div className="space-y-8">
      <h1 className="text-3xl font-bold font-headline">Admin Dashboard</h1>
      
      <Card>
        <CardHeader>
          <CardTitle>Manage Items</CardTitle>
        </CardHeader>
        <CardContent>
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead>Item Name</TableHead>
                <TableHead>Location</TableHead>
                <TableHead>Date Found</TableHead>
                <TableHead>Status</TableHead>
                <TableHead>Claimed By</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {items.map((item) => {
                const claimant = item.claimedBy ? users.find(u => u.id === item.claimedBy) : null;
                return (
                  <TableRow key={item.id}>
                    <TableCell className="font-medium">{item.name}</TableCell>
                    <TableCell>{item.location}</TableCell>
                    <TableCell>{new Date(item.dateFound).toLocaleDateString()}</TableCell>
                    <TableCell>{getStatusBadge(item.status)}</TableCell>
                    <TableCell>{claimant?.name || 'N/A'}</TableCell>
                  </TableRow>
                );
              })}
            </TableBody>
          </Table>
        </CardContent>
      </Card>

      <Card>
        <CardHeader>
          <CardTitle>Manage Users</CardTitle>
        </CardHeader>
        <CardContent>
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead>Name</TableHead>
                <TableHead>Email</TableHead>
                <TableHead>Role</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {users.map((user) => (
                <TableRow key={user.id}>
                  <TableCell className="font-medium">{user.name}</TableCell>
                  <TableCell>{user.email}</TableCell>
                  <TableCell>
                    <Badge variant="outline">{user.role.charAt(0).toUpperCase() + user.role.slice(1)}</Badge>
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </CardContent>
      </Card>
    </div>
  );
}
