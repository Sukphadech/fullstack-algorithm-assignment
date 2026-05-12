import { useState, useEffect } from "react";

function UserForm({
  onSubmit,
  selectedUser,
  clearSelection,
}) {

  const [formData, setFormData] = useState({
    name: "",
    age: "",
    email: "",
    avatar_url: "",
  });


  useEffect(() => {

    if (selectedUser) {

      setFormData(selectedUser);

    } else {

      setFormData({
        name: "",
        age: "",
        email: "",
        avatar_url: "",
      });
    }

  }, [selectedUser]);


  const handleChange = (e) => {

    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };


  const handleSubmit = (e) => {

    e.preventDefault();

    onSubmit(formData);
  };


  return (
    <form
      onSubmit={handleSubmit}
      className="
        bg-white
        p-6
        rounded-lg
        shadow
        mb-6
      "
    >

      <div className="grid md:grid-cols-2 gap-4">

        <input
          type="text"
          name="name"
          placeholder="Name"
          value={formData.name}
          onChange={handleChange}
          required
          className="p-3 border rounded"
        />

        <input
          type="number"
          name="age"
          placeholder="Age"
          value={formData.age}
          onChange={handleChange}
          required
          className="p-3 border rounded"
        />

        <input
          type="email"
          name="email"
          placeholder="Email"
          value={formData.email}
          onChange={handleChange}
          required
          className="p-3 border rounded"
        />

        <input
          type="text"
          name="avatar_url"
          placeholder="Avatar URL"
          value={formData.avatar_url}
          onChange={handleChange}
          className="p-3 border rounded"
        />

      </div>

      <div className="flex gap-3 mt-4">

        <button
          type="submit"
          className="
            px-4
            py-2
            bg-blue-600
            text-white
            rounded
          "
        >
          {selectedUser ? "Update User" : "Add User"}
        </button>

        {selectedUser && (
          <button
            type="button"
            onClick={clearSelection}
            className="
              px-4
              py-2
              bg-gray-500
              text-white
              rounded
            "
          >
            Cancel
          </button>
        )}

      </div>

    </form>
  );
}

export default UserForm;