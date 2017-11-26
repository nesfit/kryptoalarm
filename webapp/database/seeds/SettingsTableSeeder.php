<?php

use Illuminate\Database\Seeder;

class SettingsTableSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        $rows = [
            ['email_template', 'Watched address {name} {address} for {coin} was found in those transactions:' . PHP_EOL . '{txs}'],
            ['email_subject', 'Cryptoalarm notification: {name}'],
            ['email_from', 'notifications@cryptoalarm.tld'],
            ['notification_url', 'http://localhost:8000/api/notifications'],
        ];

        foreach($rows as $row) {
            DB::table('settings')->insert([
                'key' => $row[0],
                'value' => $row[1],
            ]);
        }
    }
}
