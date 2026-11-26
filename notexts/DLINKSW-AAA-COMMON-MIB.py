#
# PySNMP MIB module DLINKSW-AAA-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/dlink/DLINKSW-AAA-COMMON-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:08:25 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
dlinkIndustrialCommon, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlinkIndustrialCommon")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter32, Bits, Counter64, TimeTicks, NotificationType, Gauge32, ModuleIdentity, MibIdentifier, Unsigned32, IpAddress, ObjectIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter32", "Bits", "Counter64", "TimeTicks", "NotificationType", "Gauge32", "ModuleIdentity", "MibIdentifier", "Unsigned32", "IpAddress", "ObjectIdentity", "iso")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
dlinkSwAAACommonMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 14, 150))
dlinkSwAAACommonMIB.setRevisions(('2013-01-17 00:00',))
if mibBuilder.loadTexts: dlinkSwAAACommonMIB.setLastUpdated('201301170000Z')
if mibBuilder.loadTexts: dlinkSwAAACommonMIB.setOrganization('D-Link Corp.')
class DAaaSessionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("telnet", 1), ("console", 2), ("ssh", 3), ("http", 4))

class DAaaPrivilegeLevel(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 15)

class DAaaMethodListName(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

class DAaaMethodPriority(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 4)

class DAaaMethodName(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

dAaaCommonMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 150, 0))
dAaaMIBObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 171, 14, 150, 1))
if mibBuilder.loadTexts: dAaaMIBObjects.setStatus('current')
dAaaCommonMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 150, 2))
dAaaCommonObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 1))
if mibBuilder.loadTexts: dAaaCommonObjects.setStatus('current')
dAaaNewModelEnabled = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dAaaNewModelEnabled.setStatus('current')
dAaaCommonMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 150, 2, 1))
daaaMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 171, 14, 150, 2, 1, 1)).setObjects(("DLINKSW-AAA-COMMON-MIB", "daaaGlobalCtrlGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    daaaMIBCompliance = daaaMIBCompliance.setStatus('current')
dAaaCommonMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 150, 2, 2))
daaaGlobalCtrlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 14, 150, 2, 2, 1)).setObjects(("DLINKSW-AAA-COMMON-MIB", "dAaaNewModelEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    daaaGlobalCtrlGroup = daaaGlobalCtrlGroup.setStatus('current')
mibBuilder.exportSymbols("DLINKSW-AAA-COMMON-MIB", dlinkSwAAACommonMIB=dlinkSwAAACommonMIB, dAaaNewModelEnabled=dAaaNewModelEnabled, dAaaCommonMIBGroups=dAaaCommonMIBGroups, daaaMIBCompliance=daaaMIBCompliance, daaaGlobalCtrlGroup=daaaGlobalCtrlGroup, DAaaMethodPriority=DAaaMethodPriority, dAaaCommonObjects=dAaaCommonObjects, DAaaPrivilegeLevel=DAaaPrivilegeLevel, dAaaMIBObjects=dAaaMIBObjects, dAaaCommonMIBConformance=dAaaCommonMIBConformance, DAaaMethodListName=DAaaMethodListName, dAaaCommonMIBNotifications=dAaaCommonMIBNotifications, dAaaCommonMIBCompliances=dAaaCommonMIBCompliances, PYSNMP_MODULE_ID=dlinkSwAAACommonMIB, DAaaSessionType=DAaaSessionType, DAaaMethodName=DAaaMethodName)
