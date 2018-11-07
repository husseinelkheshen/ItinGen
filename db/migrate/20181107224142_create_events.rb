class CreateEvents < ActiveRecord::Migration[5.2]
  def change
    create_table :events do |t|
      t.string :name
      t.integer :lat
      t.integer :lng
      t.integer :rating

      t.timestamps
    end
  end
end
