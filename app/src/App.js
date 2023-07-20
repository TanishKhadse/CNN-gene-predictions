import './App.css';
import { useState } from 'react';
import Graph from './components/graph';
import Modal from './components/modal';

function App() {
  const [numEntries, setNumEntries] = useState(10)
  const [showModal, setShowModal] = useState(false)

  return (
    <div>
      <div className="App" class="flex justify-between items-center bg-gray-600 p-3 text-neutral-50 text-lg">
        <p>
          Predicting Gene Mutations Using Convolutional Neural Networks for Neurodegenerative Diseases
        </p>
        <div 
          onClick={() => setShowModal(!showModal)}
          class="
            p-2 
            text-sm 
            rounded-xl 
            w-30 
            bg-blue-500 
            hover:bg-blue-400 
            cursor-pointer
          ">
          Options 
        </div> 
      </div>
      
      <Graph />
 
      {(showModal && <Modal isOpen={showModal} onClose={() => setShowModal(false)}/>)}
    </div>
  );
}

export default App;
