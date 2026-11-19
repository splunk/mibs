#
# PySNMP MIB module CISCO-DMN-DSG-SESSIONCONTROL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-DMN-DSG-SESSIONCONTROL-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:06 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoDSGUtilities, = mibBuilder.importSymbols("CISCO-DMN-DSG-ROOT-MIB", "ciscoDSGUtilities")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
NotificationType, MibIdentifier, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, TimeTicks, IpAddress, Bits, Counter64, Gauge32, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "TimeTicks", "IpAddress", "Bits", "Counter64", "Gauge32", "Integer32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoDSGSessionControl = ModuleIdentity((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 6))
ciscoDSGSessionControl.setRevisions(('2010-08-30 11:00', '2009-11-22 15:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoDSGSessionControl.setRevisionsDescriptions(('V01.00.01 2010-08-30\n                    Updated for adherence to SNMPv2 format.', 'V01.00.00 2009-11-22\n                    Initial Version.',))
if mibBuilder.loadTexts: ciscoDSGSessionControl.setLastUpdated('201008301100Z')
if mibBuilder.loadTexts: ciscoDSGSessionControl.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoDSGSessionControl.setContactInfo('Cisco Systems, Inc.\n        Customer Service \n        Postal: 170 W Tasman Drive\n        San Jose, CA 95134\n        USA  \n        Tel: +1 800 553 NETS\n        \n        E-mail: cs-ipsla@cisco.com')
if mibBuilder.loadTexts: ciscoDSGSessionControl.setDescription('Cisco DSG Session Control MIB.')
sessionControlOpen = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 6, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("open", 1), ("writeOnly", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sessionControlOpen.setStatus('current')
if mibBuilder.loadTexts: sessionControlOpen.setDescription('Open the session. 1 indicates OPEN.')
sessionControlClose = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 6, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("saveAndClose", 1), ("ignoreAndClose", 2), ("writeOnly", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sessionControlClose.setStatus('current')
if mibBuilder.loadTexts: sessionControlClose.setDescription('Close the session.')
sessionControlStatus = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 6, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("open", 1), ("closed", 2), ("expired", 3), ("openWithInvalidConfig", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sessionControlStatus.setStatus('current')
if mibBuilder.loadTexts: sessionControlStatus.setDescription('Status of the last opened session.')
sessionControlValidateStatus = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 6, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 250))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sessionControlValidateStatus.setStatus('current')
if mibBuilder.loadTexts: sessionControlValidateStatus.setDescription('If the sessioncontrolstatus object displays invalid\n          configuration, this object displays the reason for\n          invalidity.')
mibBuilder.exportSymbols("CISCO-DMN-DSG-SESSIONCONTROL-MIB", sessionControlStatus=sessionControlStatus, PYSNMP_MODULE_ID=ciscoDSGSessionControl, sessionControlClose=sessionControlClose, sessionControlOpen=sessionControlOpen, sessionControlValidateStatus=sessionControlValidateStatus, ciscoDSGSessionControl=ciscoDSGSessionControl)
