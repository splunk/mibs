#
# PySNMP MIB module CISCO-TRUSTSEC-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-TRUSTSEC-TC-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:01 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, MibIdentifier, Counter32, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "MibIdentifier", "Counter32", "Unsigned32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoCtsTcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 694))
ciscoCtsTcMIB.setRevisions(('2013-06-06 00:00', '2012-01-30 00:00', '2009-05-14 00:00',))
if mibBuilder.loadTexts: ciscoCtsTcMIB.setLastUpdated('201306060000Z')
if mibBuilder.loadTexts: ciscoCtsTcMIB.setOrganization('Cisco Systems, Inc.')
class CtsSecurityGroupTag(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class CtsAclName(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 255)

class CtsAclNameOrEmpty(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class CtsAclList(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 255)

class CtsAclListOrEmpty(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class CtsPolicyName(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class CtsPasswordEncryptionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("other", 1), ("none", 2), ("clearText", 3), ("typeSix", 4), ("typeSeven", 5))

class CtsPassword(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

class CtsGenerationId(TextualConvention, OctetString):
    status = 'current'
    displayHint = '128a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 128)

class CtsAcsAuthorityIdentity(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class CtsCredentialRecordType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("simpleSecret", 1), ("pac", 2))

class CtsSgaclMonitorMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("on", 1), ("off", 2))

class CtsSxpConnectionStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("other", 1), ("off", 2), ("on", 3), ("pendingOn", 4), ("deleteHoldDown", 5))

mibBuilder.exportSymbols("CISCO-TRUSTSEC-TC-MIB", CtsPasswordEncryptionType=CtsPasswordEncryptionType, ciscoCtsTcMIB=ciscoCtsTcMIB, CtsGenerationId=CtsGenerationId, CtsSxpConnectionStatus=CtsSxpConnectionStatus, CtsAclListOrEmpty=CtsAclListOrEmpty, CtsAclNameOrEmpty=CtsAclNameOrEmpty, CtsSecurityGroupTag=CtsSecurityGroupTag, PYSNMP_MODULE_ID=ciscoCtsTcMIB, CtsAclList=CtsAclList, CtsCredentialRecordType=CtsCredentialRecordType, CtsPolicyName=CtsPolicyName, CtsAclName=CtsAclName, CtsPassword=CtsPassword, CtsSgaclMonitorMode=CtsSgaclMonitorMode, CtsAcsAuthorityIdentity=CtsAcsAuthorityIdentity)
