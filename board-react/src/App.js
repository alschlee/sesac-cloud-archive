import { useState } from 'react';
import './App.css';
import axios from 'axios';

function App() {
  const [title, setTitle] = useState('');
  const [contents, setContents] = useState('');
  const [user, setUser] = useState('');
  const [data, setData] = useState([]);
  const [selectedPost, setSelectedPost] = useState(null);

  const handlerTitle = e => setTitle(e.target.value);
  const handlerContents = e => setContents(e.target.value);
  const handlerUser = e => setUser(e.target.value);

  const handlerRegist = e => {
    e.preventDefault();
    axios
      .post(
        'https://uejdtb2ofc.execute-api.ap-northeast-2.amazonaws.com/prod/board',
        { title, contents, user }
      )
      .then(res => {
        console.log(res);
        setData(JSON.parse(res.data.data));
      })
      .catch(err => console.log(err));
  };

  const handleTitleClick = (item) => {
    setSelectedPost(item);
  };

  return (
    <>
      <div>
        제목 <input type="text" value={title} onChange={handlerTitle} />
      </div>
      <div>
        내용 <textarea value={contents} onChange={handlerContents} />
      </div>
      <div>
        작성자 <input type="text" value={user} onChange={handlerUser} />
      </div>
      <div>
        <button onClick={handlerRegist}>등록</button>
      </div>
      <hr />
      <table>
        <thead>
          <tr>
            <th>번호</th>
            <th>제목</th>
            <th>내용</th>
          </tr>
        </thead>
        <tbody>
          {data.map((item, index) => (
            <tr key={index}>
              <td>{item[0]}</td>
              <td onClick={() => handleTitleClick(item)} style={{ cursor: 'pointer', color: 'blue' }}>
                {item[1]}
              </td>
              <td>{item[2]}</td>
            </tr>
          ))}
        </tbody>
      </table>
      {selectedPost && (
        <div>
          <h2>상세 내용</h2>
          <p><strong>제목:</strong> {selectedPost[1]}</p>
          <p><strong>내용:</strong> {selectedPost[2]}</p>
          <p><strong>작성자:</strong> {user}</p>
        </div>
      )}
    </>
  );
}

export default App;
