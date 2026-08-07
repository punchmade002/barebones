(function () {
  "use strict";

  const subjectDocuments = {
    business: {
      title: "Leaving Certificate Business Curriculum Specification",
      path: "./relevant-resources/syllabi/business.pdf",
      sourceUrl: "https://www.curriculumonline.ie/getmedia/e81ccca9-fdf5-42e9-a291-52e9549820c9/SC-Business-Spec-ENG.pdf",
      documentType: "Curriculum specification",
      effectiveFrom: "September 2025",
      status: "Current",
    },
    pe: {
      title: "Leaving Certificate Physical Education Curriculum Specification",
      path: "./relevant-resources/syllabi/pe.pdf",
      sourceUrl: "https://www.curriculumonline.ie/getmedia/41817053-8f40-4365-8893-dba1a68508f3/LCPE_Specification_en.pdf",
      documentType: "Curriculum specification",
      effectiveFrom: "2018",
      status: "Current",
    },
    biology: {
      title: "Leaving Certificate Biology Curriculum Specification",
      path: "./relevant-resources/syllabi/biology.pdf",
      sourceUrl: "https://curriculumonline.ie/getmedia/04e86311-7225-4cf3-a723-675e33154daf/SC-BIOLOGY-Spec-ENG.pdf",
      documentType: "Curriculum specification",
      effectiveFrom: "September 2025",
      status: "Current",
    },
    geography: {
      title: "Leaving Certificate Geography Curriculum Specification",
      path: "./relevant-resources/syllabi/geography.pdf",
      sourceUrl: "https://www.curriculumonline.ie/getmedia/837bf939-b559-4b45-8c94-5590d8710083/SC-Geography-Spec-ENG-INT.pdf",
      documentType: "Curriculum specification",
      effectiveFrom: "September 2026",
      status: "Current for fifth-year students from 2026",
    },
    maths: {
      title: "Leaving Certificate Mathematics Syllabus",
      path: "./relevant-resources/syllabi/maths.pdf",
      sourceUrl: "https://www.curriculumonline.ie/getmedia/f6f2e822-2b0c-461e-bcd4-dfcde6decc0c/SCSEC25_Maths_syllabus_examination-2015_English.pdf",
      documentType: "Syllabus",
      effectiveFrom: "Examinations from 2015",
      status: "Current",
    },
    chemistry: {
      title: "Leaving Certificate Chemistry Curriculum Specification",
      path: "./relevant-resources/syllabi/chemistry.pdf",
      sourceUrl: "https://www.curriculumonline.ie/getmedia/aa7e3dd7-c156-49d2-9b2e-51cbc49c9d7e/SC-Chemistry-Specification-EN.pdf",
      documentType: "Curriculum specification",
      effectiveFrom: "September 2025",
      status: "Current",
    },
    "home-economics": {
      title: "Leaving Certificate Home Economics Scientific and Social Syllabus",
      path: "./relevant-resources/syllabi/home-economics.pdf",
      sourceUrl: "https://www.curriculumonline.ie/getmedia/b9bc688f-3a5d-48a7-90f1-b60063f49c74/SCSEC21_Home_Economics_syllabus_eng.pdf",
      documentType: "Syllabus",
      effectiveFrom: "Published syllabus",
      status: "Current",
    },
    history: {
      title: "Leaving Certificate History Syllabus",
      path: "./relevant-resources/syllabi/history.pdf",
      sourceUrl: "https://www.curriculumonline.ie/getmedia/da556505-f5fb-4921-869f-e0983fd80e50/SCSEC20_History_syllabus_eng.pdf",
      documentType: "Syllabus",
      effectiveFrom: "Published syllabus",
      status: "Current; a replacement draft was under consultation in 2026",
    },
  };

  const subjects = {};

  Object.entries(subjectDocuments).forEach(([subjectId, syllabus]) => {
    subjects[subjectId] = {
      syllabus: {
        ...syllabus,
        authority: "National Council for Curriculum and Assessment (NCCA)",
        verifiedAt: "2026-08-07",
      },
      simpleStudy: {
        source: "SimpleStudy",
        status: "awaiting-authentication",
        researchedAt: null,
        courseUrl: "",
        chapterStructure: [],
        insights: [],
        solvedExamples: [],
      },
    };
  });

  function localChapterStructure(subjectId) {
    try {
      if (typeof COURSE_DATA === "undefined" || !Array.isArray(COURSE_DATA.chapters)) return [];
      return COURSE_DATA.chapters
        .filter((chapter) => (chapter.subject || "business") === subjectId)
        .map((chapter) => ({
          id: chapter.id,
          number: chapter.number,
          title: chapter.title,
          learningOutcomes: (chapter.learningOutcomes || []).map((outcome) => ({
            id: outcome.id,
            code: outcome.code,
            title: outcome.title,
          })),
        }));
    } catch (error) {
      return [];
    }
  }

  function getSubject(subjectId) {
    const subject = subjects[subjectId];
    if (!subject) return null;
    return {
      ...subject,
      localChapterStructure: localChapterStructure(subjectId),
    };
  }

  function validate() {
    const errors = [];
    Object.entries(subjects).forEach(([subjectId, subject]) => {
      if (!subject.syllabus?.path) errors.push(`${subjectId}: missing syllabus path`);
      if (!subject.syllabus?.sourceUrl) errors.push(`${subjectId}: missing syllabus source URL`);
      if (!Array.isArray(subject.simpleStudy?.chapterStructure)) {
        errors.push(`${subjectId}: SimpleStudy chapterStructure must be an array`);
      }
      if (!Array.isArray(subject.simpleStudy?.insights)) {
        errors.push(`${subjectId}: SimpleStudy insights must be an array`);
      }
      if (!Array.isArray(subject.simpleStudy?.solvedExamples)) {
        errors.push(`${subjectId}: SimpleStudy solvedExamples must be an array`);
      }
    });
    return errors;
  }

  window.RELEVANT_RESOURCES = {
    schemaVersion: 1,
    subjects,
    getSubject,
    validate,
  };
})();
