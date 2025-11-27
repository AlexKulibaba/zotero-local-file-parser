import React, { useState, useEffect } from 'react';
import './App.css'; // This will contain Tailwind CSS directives
import { Button } from '@/components/ui/button';
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from '@/components/ui/table';
import { Dialog, DialogContent, DialogHeader, DialogTitle, DialogTrigger } from '@/components/ui/dialog';
import { ScrollArea } from '@/components/ui/scroll-area';

interface Attachment {
  id: number;
  name: string;
  type: string;
  path: string;
  is_local_file: boolean;
}

function App() {
  const [attachments, setAttachments] = useState<Attachment[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);
  const [selectedAttachment, setSelectedAttachment] = useState<Attachment | null>(null);
  const [isDialogOpen, setIsDialogOpen] = useState<boolean>(false);

  useEffect(() => {
    fetch('http://127.0.0.1:5000/api/attachments')
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then((data: Attachment[]) => {
        setAttachments(data);
        setLoading(false);
      })
      .catch((e: Error) => {
        setError(e.message);
        setLoading(false);
      });
  }, []);

  const handleViewAttachment = (attachment: Attachment) => {
    setSelectedAttachment(attachment);
    setIsDialogOpen(true);
  };

  const renderFileContent = () => {
    if (!selectedAttachment) return null;

    const fileUrl = `http://127.0.0.1:5000/api/attachments/${selectedAttachment.id}/file`;
    
    // Basic detection for PDF vs. image. More types could be added.
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
        // For HTML, we can also use an iframe. Be aware of potential security risks with untrusted HTML.
        return (
            <iframe
                src={fileUrl}
                title={selectedAttachment.name}
                className="w-full h-[80vh]"
                sandbox="allow-scripts allow-same-origin" // Basic sandbox for security
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

      <ScrollArea className="h-[70vh] w-full rounded-md border">
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead className="w-[50px]">ID</TableHead>
              <TableHead>Name</TableHead>
              <TableHead>Type</TableHead>
              <TableHead className="text-right">Actions</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {attachments.map((attachment) => (
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