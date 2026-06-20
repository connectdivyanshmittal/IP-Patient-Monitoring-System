#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <windows.h>

#define BAR_LEN 20

// Function to display progress bar
void display_bar(int value, int max_len) {
    int bars = (value * max_len) / 100;
    printf("[");
    for (int i = 0; i < bars; i++) printf("#");
    for (int i = bars; i < max_len; i++) printf(" ");
    printf("]");
}

// Function to read and display one line of CSV
int read_next(FILE *fp, char *patient_id, char *timestamp, int *hr, int *spo2, float *temp) {
    char line[256];
    if (fgets(line, sizeof(line), fp) == NULL) return 0; // EOF

    sscanf(line, "%[^,],%[^,],%d,%d,%f", patient_id, timestamp, hr, spo2, temp);
    return 1;
}

int main() {
    FILE *fp1, *fp2;
    char line1[256], line2[256];
    char patient_id1[50], patient_id2[50];
    char timestamp1[50], timestamp2[50];
    int hr1, hr2, spo21, spo22;
    float temp1, temp2;

    fp1 = fopen("patient_001_data.csv", "r");
    fp2 = fopen("patient_002_data.csv", "r");

    if (fp1 == NULL || fp2 == NULL) {
        printf("Error: Unable to open one or both CSV files!\n");
        return 1;
    }

    // Skip headers
    fgets(line1, sizeof(line1), fp1);
    fgets(line2, sizeof(line2), fp2);

    printf("\n================ LIVE PATIENT MONITORING ================\n");

    while (1) {
        int r1 = read_next(fp1, patient_id1, timestamp1, &hr1, &spo21, &temp1);
        int r2 = read_next(fp2, patient_id2, timestamp2, &hr2, &spo22, &temp2);

        if (!r1 && !r2) break; // both files finished

        system("cls"); // clear screen for live effect

        printf("------------------------------------------------------------\n");
        printf("Patient 1: %s  |  Time: %s\n", patient_id1, timestamp1);
        printf("Heart Rate : %3d bpm ", hr1);
        display_bar(hr1, BAR_LEN); printf("\n");
        printf("SpO2       : %3d%%   ", spo21);
        display_bar(spo21, BAR_LEN); printf("\n");
        printf("Temperature: %.1f °C ", temp1);
        display_bar((int)((temp1 - 36.0) * 40), BAR_LEN);
        printf("\n------------------------------------------------------------\n");

        printf("Patient 2: %s  |  Time: %s\n", patient_id2, timestamp2);
        printf("Heart Rate : %3d bpm ", hr2);
        display_bar(hr2, BAR_LEN); printf("\n");
        printf("SpO2       : %3d%%   ", spo22);
        display_bar(spo22, BAR_LEN); printf("\n");
        printf("Temperature: %.1f °C ", temp2);
        display_bar((int)((temp2 - 36.0) * 40), BAR_LEN);
        printf("\n------------------------------------------------------------\n");

        Sleep(1000); // 1-second delay for live simulation
    }

    fclose(fp1);
    fclose(fp2);
    printf("\nFinished displaying readings for both patients!\n");

    return 0;
}
