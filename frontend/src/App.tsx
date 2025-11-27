import React, { useState, useEffect, useMemo } from 'react';
import './App.css'; // This will contain Tailwind CSS directives
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from '@/components/ui/table';
import { Dialog, DialogContent, DialogHeader, DialogTitle } from '@/components/ui/dialog';
import { ScrollArea } from '@/components/ui/scroll-area';

interface Attachment {
  id: number;
  name: string;
  type: string;
  path: string;
  is_local_file: boolean;
}

type SortKey = keyof Attachment;

function App() {
  const [attachments, setAttachments] = useState<Attachment[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);
  const [selectedAttachment, setSelectedAttachment] = useState<Attachment | null>(null);
  const [isDialogOpen, setIsDialogOpen] = useState<boolean>(false);
  const [sortKey, setSortKey] = useState<SortKey>('id');
  const [sortDirection, setSortDirection] = useState<'asc' | 'desc'>('asc');
  const [searchTerm, setSearchTerm] = useState<string>('');
  const [currentPage, setCurrentPage] = useState<number>(1);
  const [totalPages, setTotalPages] = useState<number>(1);

  useEffect(() => {
    setLoading(true);
    fetch(`http://127.0.0.1:5000/api/attachments?page=${currentPage}&per_page=50`)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        setAttachments(data.attachments);
        setTotalPages(Math.ceil(data.total / data.per_page));
        setLoading(false);
      })
      .catch((e: Error) => {
        setError(e.message);
        setLoading(false);
      });
  }, [currentPage]);

  const filteredAndSortedAttachments = useMemo(() => {
    const filtered = attachments.filter(
      (attachment) =>
        attachment.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
        attachment.type.toLowerCase().includes(searchTerm.toLowerCase())
    );

    const sorted = [...filtered].sort((a, b) => {
      if (a[sortKey] < b[sortKey]) {
        return sortDirection === 'asc' ? -1 : 1;
      }
      if (a[sortKey] > b[sortKey]) {
        return sortDirection === 'asc' ? 1 : -1;
      }
      return 0;
    });
    return sorted;
  }, [attachments, sortKey, sortDirection, searchTerm]);

  const handleSort = (key: SortKey) => {
    if (sortKey === key) {
      setSortDirection(sortDirection === 'asc' ? 'desc' : 'asc');
    } else {
      setSortKey(key);
      setSortDirection('asc');
    }
  };

  const handleViewAttachment = (attachment: Attachment) => {
    setSelectedAttachment(attachment);
    setIsDialogOpen(true);
  };

  const renderFileContent = () => {
    if (!selectedAttachment) return null;

    const fileUrl = `http://127.0.0.1:5000/api/attachments/${selectedAttachment.id}/file`;
    
    if (selectedAttachment.type.includes('pdf')) {
      return (
        <iframe 
          src={fileUrl} 
          title={selectedAttachment.name} 
          className="w-full h-[80vh]" 
          allowFullScreen
        ></iframe>
      );
    } else if (selectedAttachment.type.includes('image')) {
      return <img src={fileUrl} alt={selectedAttachment.name} className="max-w-full max-h-[80vh] object-contain" />;
    } else if (selectedAttachment.type.includes('html')) {
        return (
            <iframe
                src={fileUrl}
                title={selectedAttachment.name}
                className="w-full h-[80vh]"
                sandbox="allow-scripts allow-same-origin"
            ></iframe>
        );
    }
    
    return <p>Preview not available for this file type ({selectedAttachment.type}).</p>;
  };

  if (loading) {
    return <div className="p-4">Loading attachments...</div>;
  }

  if (error) {
    return <div className="p-4 text-red-500">Error: {error}</div>;
  }

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Local Zotero Attachments</h1>

      <div className="mb-4">
        <Input
          type="text"
          placeholder="Search by name or type..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
        />
      </div>

      <ScrollArea className="h-[70vh] w-full rounded-md border">
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead className="w-[50px] cursor-pointer" onClick={() => handleSort('id')}>
                ID {sortKey === 'id' && (sortDirection === 'asc' ? '▲' : '▼')}
              </TableHead>
              <TableHead className="cursor-pointer" onClick={() => handleSort('name')}>
                Name {sortKey === 'name' && (sortDirection === 'asc' ? '▲' : '▼')}
              </TableHead>
              <TableHead className="cursor-pointer" onClick={() => handleSort('type')}>
                Type {sortKey === 'type' && (sortDirection === 'asc' ? '▲' : '▼')}
              </TableHead>
              <TableHead className="text-right">Actions</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {filteredAndSortedAttachments.map((attachment) => (
              <TableRow key={attachment.id}>
                <TableCell className="font-medium">{attachment.id}</TableCell>
                <TableCell>{attachment.name}</TableCell>
                <TableCell>{attachment.type}</TableCell>
                <TableCell className="text-right">
                  <Button onClick={() => handleViewAttachment(attachment)} size="sm">
                    View
                  </Button>
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </ScrollArea>
      <div className="flex justify-between items-center mt-4">
        <Button onClick={() => setCurrentPage(prev => Math.max(prev - 1, 1))} disabled={currentPage === 1}>
          Previous
        </Button>
        <span>Page {currentPage} of {totalPages}</span>
        <Button onClick={() => setCurrentPage(prev => Math.min(prev + 1, totalPages))} disabled={currentPage === totalPages}>
          Next
        </Button>
      </div>

      <Dialog open={isDialogOpen} onOpenChange={setIsDialogOpen}>
        <DialogContent className="min-w-[90vw] min-h-[90vh]">
          <DialogHeader>
            <DialogTitle>{selectedAttachment?.name}</DialogTitle>
          </DialogHeader>
          <div className="w-full h-full flex justify-center items-center">
            {renderFileContent()}
          </div>
        </DialogContent>
      </Dialog>
    </div>
  );
}

export default App;