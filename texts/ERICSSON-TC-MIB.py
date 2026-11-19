#
# PySNMP MIB module ERICSSON-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ericsson/ERICSSON-TC-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:36:15 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ericssonModules, = mibBuilder.importSymbols("ERICSSON-TOP-MIB", "ericssonModules")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ObjectIdentity, MibIdentifier, Gauge32, TimeTicks, ModuleIdentity, IpAddress, Integer32, Bits, iso, Counter32, Unsigned32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ObjectIdentity", "MibIdentifier", "Gauge32", "TimeTicks", "ModuleIdentity", "IpAddress", "Integer32", "Bits", "iso", "Counter32", "Unsigned32", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ericssonTCMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 193, 183, 1))
ericssonTCMIB.setRevisions(('2021-02-04 00:00', '2017-08-11 00:00', '2017-04-13 00:00', '2016-06-24 00:00', '2008-10-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ericssonTCMIB.setRevisionsDescriptions(('Removed employee Id from CONTACT-INFO.\r\n                                Document number: 2/196 03-CXC 172 7549, Rev E.', "Updated description for EriPath;\r\n                                Added more detail to DESCRIPTION for each REVISION\r\n                                Removed author's name.\r\n                                Document number: 2/196 03-CXC 172 7549, Rev D.", 'Updated REFERENCE clause for EriPath:\r\n                                        - Added YANG module ericsson-yang-types;\r\n                                        - Updated YANG RFC reference to YANG 1.1 RFC.\r\n                                Document number: 2/196 03-CXC 172 7549, Rev C.', 'Updated version of this MIB module. Included XPath\r\n                                instance identifier.\r\n                                Document number: 2/196 03-CXC 172 7549, Rev B.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ericssonTCMIB.setLastUpdated('202102040000Z')
if mibBuilder.loadTexts: ericssonTCMIB.setOrganization('Ericsson AB')
if mibBuilder.loadTexts: ericssonTCMIB.setContactInfo('IMF')
if mibBuilder.loadTexts: ericssonTCMIB.setDescription('This MIB document includes textual conventions\r\n                that can be used by all of the Ericsson group.\r\n                The intention is to have shared definitions such\r\n                that integration and SNMP development are made\r\n                easier.')
class EriMO(TextualConvention, OctetString):
    reference = '3GPP TS 32.300 V7.2, Name convention for\r\n                Managed Objects'
    description = "The 3GPP naming convention shall be used as the\r\n                format for the managed object parameter.  Note\r\n                that the granularity MUST be sufficient to\r\n                guarantee unique alarm states and relevant\r\n                resource identification to the operator.  \r\n                                NOTE: The DN should be *relative* to the Managed \r\n                                Element's *own* root."
    status = 'current'
    displayHint = '1a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 150)

class EriPath(TextualConvention, OctetString):
    reference = 'YANG module ericsson-yang-types;\r\n                                RFC 7950 , The YANG 1.1 Data Modeling Language'
    description = "An abridged instance-identifier in YANG that references a \r\n                                resource within the Managed Element. \r\n                                For example: \r\n                                /ex:system/server[ip='192.0.2.1'][port='80']\r\n                                See: YANG module ericsson-yang-types.\r\n                                See also: RFC 7950 Section 9.13.\r\n                                NOTE: The granularity must be good enough to guarantee \r\n                                unique alarm states and relevant resource identification \r\n                                to the operator."
    status = 'current'
    displayHint = '1a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 150)

mibBuilder.exportSymbols("ERICSSON-TC-MIB", EriMO=EriMO, ericssonTCMIB=ericssonTCMIB, EriPath=EriPath, PYSNMP_MODULE_ID=ericssonTCMIB)
