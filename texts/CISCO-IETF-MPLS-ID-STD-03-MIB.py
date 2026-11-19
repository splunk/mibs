#
# PySNMP MIB module CISCO-IETF-MPLS-ID-STD-03-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-IETF-MPLS-ID-STD-03-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:06 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
CMplsIccId, CMplsGlobalId, CMplsNodeId = mibBuilder.importSymbols("CISCO-MPLS-TC-EXT-STD-MIB", "CMplsIccId", "CMplsGlobalId", "CMplsNodeId")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
mplsStdMIB, = mibBuilder.importSymbols("MPLS-TC-STD-MIB", "mplsStdMIB")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
NotificationType, MibIdentifier, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, TimeTicks, IpAddress, Bits, Counter64, Gauge32, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "TimeTicks", "IpAddress", "Bits", "Counter64", "Gauge32", "Integer32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cmplsIdStdMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 147))
cmplsIdStdMIB.setRevisions(('2012-04-08 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cmplsIdStdMIB.setRevisionsDescriptions(('MPLS identifiers mib object extension',))
if mibBuilder.loadTexts: cmplsIdStdMIB.setLastUpdated('201206070000Z')
if mibBuilder.loadTexts: cmplsIdStdMIB.setOrganization('Multiprotocol Label Switching (MPLS) Working Group')
if mibBuilder.loadTexts: cmplsIdStdMIB.setContactInfo('Venkatesan Mahalingam\n            Dell Inc,\n            350 Holger way, San Jose, CA, USA\n            Email: venkat.mahalingams@gmail.com\n\n            Kannan KV Sampath\n            Aricent,\n            India\n            Email: Kannan.Sampath@aricent.com\n\n            Sam Aldrin\n            Huawei Technologies\n            2330 Central Express Way,\n            Santa Clara, CA 95051, USA\n            Email:  aldrin.ietf@gmail.com\n\n            Thomas D. Nadeau\n            Juniper Networks\n            10 Technology Park Drive, Westford, MA 01886\n            Email: tnadeau@juniper.net')
if mibBuilder.loadTexts: cmplsIdStdMIB.setDescription('Copyright (c) 2012 IETF Trust and the persons identified\n        as the document authors.  All rights reserved.\n\n        This MIB module contains generic object definitions for\n        MPLS Traffic Engineering in transport networks. This module is a\n        cisco-ized version of the IETF draft:\n        draft-ietf-mpls-tp-te-mib-03.')
cmplsIdNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 147, 0))
cmplsIdObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 147, 1))
cmplsIdConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 147, 2))
cmplsGlobalId = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 147, 1, 1), CMplsGlobalId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmplsGlobalId.setReference('MPLS-TP Identifiers [RFC6370].')
if mibBuilder.loadTexts: cmplsGlobalId.setStatus('current')
if mibBuilder.loadTexts: cmplsGlobalId.setDescription('This object allows the administrator to assign a unique\n        operator identifier also called MPLS-TP Global_ID.')
cmplsIcc = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 147, 1, 2), CMplsIccId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmplsIcc.setReference('MPLS-TP Identifiers [RFC6370].')
if mibBuilder.loadTexts: cmplsIcc.setStatus('current')
if mibBuilder.loadTexts: cmplsIcc.setDescription('This object allows the operator or service provider to\n        assign a unique MPLS-TP ITU-T Carrier Code (ICC) to a\n        network.')
cmplsNodeId = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 147, 1, 3), CMplsNodeId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmplsNodeId.setReference('MPLS-TP Identifiers [RFC6370].')
if mibBuilder.loadTexts: cmplsNodeId.setStatus('current')
if mibBuilder.loadTexts: cmplsNodeId.setDescription('This object allows the operator or service provider to\n        assign a unique MPLS-TP Node_ID.\n\n        The Node_ID is assigned within the scope of\n        the Global_ID.')
cmplsIdGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 147, 2, 1))
cmplsIdCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 147, 2, 2))
cmplsIdModuleFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 147, 2, 2, 1)).setObjects(("CISCO-IETF-MPLS-ID-STD-03-MIB", "cmplsIdScalarGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmplsIdModuleFullCompliance = cmplsIdModuleFullCompliance.setStatus('current')
if mibBuilder.loadTexts: cmplsIdModuleFullCompliance.setDescription('Compliance statement for agents that provide full\n        support the MPLS-ID-STD-MIB module.')
cmplsIdModuleReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 147, 2, 2, 2)).setObjects(("CISCO-IETF-MPLS-ID-STD-03-MIB", "cmplsIdScalarGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmplsIdModuleReadOnlyCompliance = cmplsIdModuleReadOnlyCompliance.setStatus('current')
if mibBuilder.loadTexts: cmplsIdModuleReadOnlyCompliance.setDescription('Compliance statement for agents that provide full\n        support the MPLS-ID-STD-MIB module.')
cmplsIdScalarGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 147, 2, 1, 1)).setObjects(("CISCO-IETF-MPLS-ID-STD-03-MIB", "cmplsGlobalId"), ("CISCO-IETF-MPLS-ID-STD-03-MIB", "cmplsNodeId"), ("CISCO-IETF-MPLS-ID-STD-03-MIB", "cmplsIcc"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmplsIdScalarGroup = cmplsIdScalarGroup.setStatus('current')
if mibBuilder.loadTexts: cmplsIdScalarGroup.setDescription('Scalar object needed to implement MPLS TP path.')
mibBuilder.exportSymbols("CISCO-IETF-MPLS-ID-STD-03-MIB", PYSNMP_MODULE_ID=cmplsIdStdMIB, cmplsIdObjects=cmplsIdObjects, cmplsIdModuleFullCompliance=cmplsIdModuleFullCompliance, cmplsIdStdMIB=cmplsIdStdMIB, cmplsIdGroups=cmplsIdGroups, cmplsIdScalarGroup=cmplsIdScalarGroup, cmplsIdNotifications=cmplsIdNotifications, cmplsIdConformance=cmplsIdConformance, cmplsIdModuleReadOnlyCompliance=cmplsIdModuleReadOnlyCompliance, cmplsIdCompliances=cmplsIdCompliances, cmplsGlobalId=cmplsGlobalId, cmplsIcc=cmplsIcc, cmplsNodeId=cmplsNodeId)
