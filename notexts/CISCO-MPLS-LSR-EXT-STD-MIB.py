#
# PySNMP MIB module CISCO-MPLS-LSR-EXT-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-MPLS-LSR-EXT-STD-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:58 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
mplsInSegmentGroup, mplsXCIndex, mplsXCGroup, mplsPerfGroup, mplsXCOutSegmentIndex, mplsLsrNotificationGroup, mplsOutSegmentGroup, mplsXCInSegmentIndex = mibBuilder.importSymbols("MPLS-LSR-STD-MIB", "mplsInSegmentGroup", "mplsXCIndex", "mplsXCGroup", "mplsPerfGroup", "mplsXCOutSegmentIndex", "mplsLsrNotificationGroup", "mplsOutSegmentGroup", "mplsXCInSegmentIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, TimeTicks, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, RowPointer, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowPointer", "TextualConvention")
cmplsLsrExtStdMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 145))
cmplsLsrExtStdMIB.setRevisions(('2012-02-22 00:00',))
if mibBuilder.loadTexts: cmplsLsrExtStdMIB.setLastUpdated('201204300000Z')
if mibBuilder.loadTexts: cmplsLsrExtStdMIB.setOrganization('Multiprotocol Label Switching (MPLS) Working Group')
cmplsLsrExtNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 145, 0))
cmplsLsrExtObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 145, 1))
cmplsLsrExtConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 145, 2))
cmplsXCExtTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 145, 1, 1), )
if mibBuilder.loadTexts: cmplsXCExtTable.setStatus('current')
cmplsXCExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 145, 1, 1, 1), ).setIndexNames((0, "MPLS-LSR-STD-MIB", "mplsXCIndex"), (0, "MPLS-LSR-STD-MIB", "mplsXCInSegmentIndex"), (0, "MPLS-LSR-STD-MIB", "mplsXCOutSegmentIndex"))
if mibBuilder.loadTexts: cmplsXCExtEntry.setStatus('current')
cmplsXCExtTunnelPointer = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 145, 1, 1, 1, 1), RowPointer()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmplsXCExtTunnelPointer.setStatus('current')
cmplsXCOppositeDirXCPtr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 145, 1, 1, 1, 2), RowPointer()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmplsXCOppositeDirXCPtr.setStatus('current')
cmplsLsrExtGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 145, 2, 1))
cmplsLsrExtCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 145, 2, 2))
cmplsLsrExtModuleFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 145, 2, 2, 1)).setObjects(("MPLS-LSR-STD-MIB", "mplsInSegmentGroup"), ("MPLS-LSR-STD-MIB", "mplsOutSegmentGroup"), ("MPLS-LSR-STD-MIB", "mplsXCGroup"), ("MPLS-LSR-STD-MIB", "mplsPerfGroup"), ("MPLS-LSR-STD-MIB", "mplsLsrNotificationGroup"), ("CISCO-MPLS-LSR-EXT-STD-MIB", "cmplsXCExtGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmplsLsrExtModuleFullCompliance = cmplsLsrExtModuleFullCompliance.setStatus('current')
cmplsLsrExtModuleReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 145, 2, 2, 2)).setObjects(("MPLS-LSR-STD-MIB", "mplsInterfaceGroup"), ("MPLS-LSR-STD-MIB", "mplsInSegmentGroup"), ("MPLS-LSR-STD-MIB", "mplsOutSegmentGroup"), ("MPLS-LSR-STD-MIB", "mplsXCGroup"), ("MPLS-LSR-STD-MIB", "mplsPerfGroup"), ("CISCO-MPLS-LSR-EXT-STD-MIB", "cmplsXCExtGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmplsLsrExtModuleReadOnlyCompliance = cmplsLsrExtModuleReadOnlyCompliance.setStatus('current')
cmplsXCExtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 145, 2, 1, 1)).setObjects(("CISCO-MPLS-LSR-EXT-STD-MIB", "cmplsXCExtTunnelPointer"), ("CISCO-MPLS-LSR-EXT-STD-MIB", "cmplsXCOppositeDirXCPtr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmplsXCExtGroup = cmplsXCExtGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-MPLS-LSR-EXT-STD-MIB", cmplsLsrExtCompliances=cmplsLsrExtCompliances, cmplsLsrExtModuleReadOnlyCompliance=cmplsLsrExtModuleReadOnlyCompliance, cmplsLsrExtConformance=cmplsLsrExtConformance, cmplsXCOppositeDirXCPtr=cmplsXCOppositeDirXCPtr, cmplsLsrExtStdMIB=cmplsLsrExtStdMIB, cmplsXCExtEntry=cmplsXCExtEntry, cmplsLsrExtModuleFullCompliance=cmplsLsrExtModuleFullCompliance, cmplsXCExtTunnelPointer=cmplsXCExtTunnelPointer, PYSNMP_MODULE_ID=cmplsLsrExtStdMIB, cmplsXCExtGroup=cmplsXCExtGroup, cmplsLsrExtGroups=cmplsLsrExtGroups, cmplsXCExtTable=cmplsXCExtTable, cmplsLsrExtObjects=cmplsLsrExtObjects, cmplsLsrExtNotifications=cmplsLsrExtNotifications)
