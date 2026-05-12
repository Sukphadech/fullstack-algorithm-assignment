import { useEffect, useState } from "react";

import {
  getUsers,
  createUser,
  updateUser,
  deleteUser,
} from "./api/userApi";

import UserTable from "./components/UserTable";
import UserForm from "./components/UserForm";
import SearchBox from "./components/SearchBox";
import Pagination from "./components/Pagination";


function App() {

  const [users, setUsers] = useState([]);

  const [loading, setLoading] = useState(true);

  const [search, setSearch] = useState("");

  const [start, setStart] = useState(0);

  const [selectedUser, setSelectedUser] =
    useState(null);

  const limit = 5;

  const [total, setTotal] = useState(0);


  useEffect(() => {
    fetchUsers();
  }, [search, start]);


  const fetchUsers = async () => {

    try {

      setLoading(true);

      const data = await getUsers(
        search,
        start,
        limit
      );

      setUsers(data.data);

      setTotal(data.total);

    } catch (error) {

      console.error(error);

    } finally {

      setLoading(false);
    }
  };


  const handleSearch = (value) => {

    setSearch(value);

    setStart(0);
  };


  const handleSubmit = async (formData) => {

    try {

      if (selectedUser) {

        await updateUser(
          selectedUser.id,
          formData
        );

      } else {

        await createUser(formData);
      }

      setSelectedUser(null);

      fetchUsers();

    } catch (error) {

      alert(
        error.response?.data?.detail ||
        "Something went wrong"
      );
    }
  };


  const handleEdit = (user) => {

    setSelectedUser(user);
  };


  const handleDelete = async (userId) => {

    const confirmed = window.confirm(
      "Delete this user?"
    );

    if (!confirmed) return;

    try {

      await deleteUser(userId);

      fetchUsers();

    } catch (error) {

      console.error(error);
    }
  };


  return (
    
    <div className="min-h-screen bg-gray-100 p-8">
      <h1 className="text-3xl font-bold text-center mb-6">
        
        User Management System
      </h1>
      

      <UserForm
        onSubmit={handleSubmit}
        selectedUser={selectedUser}
        clearSelection={() =>
          setSelectedUser(null)
        }
      />

      <div className="flex justify-between items-center mb-4">

        <SearchBox
          search={search}
          setSearch={handleSearch}
        />

      </div>


      {loading ? (

        <p className="text-center">
          Loading...
        </p>

      ) : users.length === 0 ? (

        <p className="text-center">
          <div className="text-center py-10">
          <p className="text-gray-500 text-lg">
            No users found
          </p>
        </div>
        </p>

      ) : (

        <>
          <UserTable
            users={users}
            onEdit={handleEdit}
            onDelete={handleDelete}
          />

          <Pagination
            start={start}
            limit={limit}
            total={total}
            setStart={setStart}
          />
        </>
      )}

    </div>
  );
}

export default App;