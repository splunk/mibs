#
# PySNMP MIB module CISCO-DTI-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-DTI-EXT-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:58 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
dtiProtocolServerStatusFlag, dtiProtocolClientStatusFlag = mibBuilder.importSymbols("DTI-MIB", "dtiProtocolServerStatusFlag", "dtiProtocolClientStatusFlag")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
ciscoDtiExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 822))
ciscoDtiExtMIB.setRevisions(('2014-08-22 00:00',))
if mibBuilder.loadTexts: ciscoDtiExtMIB.setLastUpdated('201408220000Z')
if mibBuilder.loadTexts: ciscoDtiExtMIB.setOrganization('Cisco Systems, Inc.')
ciscoDtiExtNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 822, 0))
ciscoDtiExtObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 822, 1))
ciscoDtiExtConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 822, 2))
cdeServerStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 822, 0, 1)).setObjects(("DTI-MIB", "dtiProtocolServerStatusFlag"))
if mibBuilder.loadTexts: cdeServerStatusChange.setStatus('current')
cdeClientStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 822, 0, 2)).setObjects(("DTI-MIB", "dtiProtocolClientStatusFlag"))
if mibBuilder.loadTexts: cdeClientStatusChange.setStatus('current')
ciscoDtiExtCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 822, 2, 1))
cdeServerStatusChangeEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 822, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdeServerStatusChangeEnable.setStatus('current')
cdeClientStatusChangeEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 822, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdeClientStatusChangeEnable.setStatus('current')
ciscoDtiExtGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 822, 2, 2))
ciscoDtiExtCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 822, 2, 1, 1)).setObjects(("CISCO-DTI-EXT-MIB", "ciscoDtiExtNotifsControlGroup"), ("CISCO-DTI-EXT-MIB", "ciscoDtiExtNotifsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDtiExtCompliance = ciscoDtiExtCompliance.setStatus('current')
ciscoDtiExtNotifsControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 822, 2, 2, 1)).setObjects(("CISCO-DTI-EXT-MIB", "cdeServerStatusChangeEnable"), ("CISCO-DTI-EXT-MIB", "cdeClientStatusChangeEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDtiExtNotifsControlGroup = ciscoDtiExtNotifsControlGroup.setStatus('current')
ciscoDtiExtNotifsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 822, 2, 2, 2)).setObjects(("CISCO-DTI-EXT-MIB", "cdeServerStatusChange"), ("CISCO-DTI-EXT-MIB", "cdeClientStatusChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDtiExtNotifsGroup = ciscoDtiExtNotifsGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-DTI-EXT-MIB", ciscoDtiExtNotifs=ciscoDtiExtNotifs, ciscoDtiExtMIB=ciscoDtiExtMIB, ciscoDtiExtObjects=ciscoDtiExtObjects, cdeServerStatusChange=cdeServerStatusChange, ciscoDtiExtCompliances=ciscoDtiExtCompliances, cdeServerStatusChangeEnable=cdeServerStatusChangeEnable, ciscoDtiExtNotifsGroup=ciscoDtiExtNotifsGroup, ciscoDtiExtGroups=ciscoDtiExtGroups, ciscoDtiExtCompliance=ciscoDtiExtCompliance, cdeClientStatusChange=cdeClientStatusChange, PYSNMP_MODULE_ID=ciscoDtiExtMIB, ciscoDtiExtConform=ciscoDtiExtConform, cdeClientStatusChangeEnable=cdeClientStatusChangeEnable, ciscoDtiExtNotifsControlGroup=ciscoDtiExtNotifsControlGroup)
