#
# PySNMP MIB module CISCO-IETF-MPLS-ID-STD-03-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-IETF-MPLS-ID-STD-03-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:00 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
CMplsGlobalId, CMplsIccId, CMplsNodeId = mibBuilder.importSymbols("CISCO-MPLS-TC-EXT-STD-MIB", "CMplsGlobalId", "CMplsIccId", "CMplsNodeId")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
mplsStdMIB, = mibBuilder.importSymbols("MPLS-TC-STD-MIB", "mplsStdMIB")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, TimeTicks, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cmplsIdStdMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 147))
cmplsIdStdMIB.setRevisions(('2012-04-08 00:00',))
if mibBuilder.loadTexts: cmplsIdStdMIB.setLastUpdated('201206070000Z')
if mibBuilder.loadTexts: cmplsIdStdMIB.setOrganization('Multiprotocol Label Switching (MPLS) Working Group')
cmplsIdNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 147, 0))
cmplsIdObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 147, 1))
cmplsIdConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 147, 2))
cmplsGlobalId = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 147, 1, 1), CMplsGlobalId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmplsGlobalId.setStatus('current')
cmplsIcc = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 147, 1, 2), CMplsIccId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmplsIcc.setStatus('current')
cmplsNodeId = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 147, 1, 3), CMplsNodeId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmplsNodeId.setStatus('current')
cmplsIdGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 147, 2, 1))
cmplsIdCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 147, 2, 2))
cmplsIdModuleFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 147, 2, 2, 1)).setObjects(("CISCO-IETF-MPLS-ID-STD-03-MIB", "cmplsIdScalarGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmplsIdModuleFullCompliance = cmplsIdModuleFullCompliance.setStatus('current')
cmplsIdModuleReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 147, 2, 2, 2)).setObjects(("CISCO-IETF-MPLS-ID-STD-03-MIB", "cmplsIdScalarGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmplsIdModuleReadOnlyCompliance = cmplsIdModuleReadOnlyCompliance.setStatus('current')
cmplsIdScalarGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 147, 2, 1, 1)).setObjects(("CISCO-IETF-MPLS-ID-STD-03-MIB", "cmplsGlobalId"), ("CISCO-IETF-MPLS-ID-STD-03-MIB", "cmplsNodeId"), ("CISCO-IETF-MPLS-ID-STD-03-MIB", "cmplsIcc"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmplsIdScalarGroup = cmplsIdScalarGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-IETF-MPLS-ID-STD-03-MIB", cmplsIcc=cmplsIcc, PYSNMP_MODULE_ID=cmplsIdStdMIB, cmplsNodeId=cmplsNodeId, cmplsIdObjects=cmplsIdObjects, cmplsIdModuleFullCompliance=cmplsIdModuleFullCompliance, cmplsIdConformance=cmplsIdConformance, cmplsIdScalarGroup=cmplsIdScalarGroup, cmplsGlobalId=cmplsGlobalId, cmplsIdCompliances=cmplsIdCompliances, cmplsIdGroups=cmplsIdGroups, cmplsIdModuleReadOnlyCompliance=cmplsIdModuleReadOnlyCompliance, cmplsIdNotifications=cmplsIdNotifications, cmplsIdStdMIB=cmplsIdStdMIB)
